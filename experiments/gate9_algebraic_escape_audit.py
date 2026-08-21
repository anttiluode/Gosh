#!/usr/bin/env python3
"""
Gate 9 — algebraic escape audit.

Question left by Gate 8:
Can an exact discontinuous/algebraic invariant (rank, determinant, minors,
characteristic-polynomial data) distinguish an off-line reflected pair from
its double-on-line limit without paying the finite-resolution / higher-
correlation costs that defeated the continuous observables?

No RH claim. This script checks two structural facts.

1. Local 2x2 pair block:
      u(a)=[1,1+i a]
      H(a)=u u^T + conj(u) conj(u)^T
   has
      det H(a) = -4 a^2.
   Thus rank/determinant detect every a!=0 exactly, but the determinant sign
   loses robustness under an operator perturbation of size |lambda_-(a)|~a^2.

2. Global translation-invariant Gram data:
   for the Gate-1 homometric sets A,B, the first two elementary symmetric
   spectral invariants e1,e2 tie because they are functions of tr G and tr G^2.
   e3 separates as soon as tr G^3 separates. The full determinant e_n is simply
   the top exterior-power invariant. Newton identities make the correlation-
   order ladder explicit rather than magical.

Dependency: numpy.
"""

import json
from pathlib import Path

import numpy as np

OUT = Path("results")
OUT.mkdir(exist_ok=True)

A = np.array([0, 1, 4, 10, 12, 17], dtype=float)
B = np.array([0, 1, 8, 11, 13, 17], dtype=float)
THETA = 0.4


def H(a: float) -> np.ndarray:
    u = np.array([1.0 + 0j, 1.0 + 1j * a])
    return (np.outer(u, u) + np.outer(np.conj(u), np.conj(u))).real


def gram(points: np.ndarray, theta: float = THETA) -> np.ndarray:
    d = points[:, None] - points[None, :]
    return np.sinc(theta * d)


def power_sums(G: np.ndarray, kmax: int):
    p = {}
    P = np.eye(G.shape[0])
    for k in range(1, kmax + 1):
        P = P @ G
        p[k] = float(np.trace(P))
    return p


def elementary_from_power(p, kmax: int):
    # Newton identities:
    #   k e_k = sum_{i=1}^k (-1)^(i-1) e_{k-i} p_i.
    e = [1.0]
    for k in range(1, kmax + 1):
        s = 0.0
        for i in range(1, k + 1):
            s += ((-1) ** (i - 1)) * e[k - i] * p[i]
        e.append(s / k)
    return e


def main():
    local_rows = []
    for a in [1e-1, 3e-2, 1e-2, 3e-3, 1e-3, 1e-4]:
        M = H(a)
        evals, evecs = np.linalg.eigh(M)
        lam_minus = float(evals[0])
        v_minus = evecs[:, 0]

        # The smallest operator perturbation that can push the negative
        # eigenvalue to zero is |lambda_-| in its own eigendirection.
        E_to_zero = (-lam_minus) * np.outer(v_minus, v_minus)
        M_zero = M + E_to_zero

        # A 1% larger perturbation flips the local determinant positive.
        E_flip = 1.01 * E_to_zero
        M_flip = M + E_flip

        local_rows.append({
            "a": a,
            "det_H": float(np.linalg.det(M)),
            "det_over_minus4a2": float(np.linalg.det(M) / (-4.0 * a * a)),
            "lambda_minus": lam_minus,
            "abs_lambda_minus_over_a2": abs(lam_minus) / (a * a),
            "operator_error_to_rank_boundary": float(np.linalg.norm(E_to_zero, 2)),
            "error_to_boundary_over_a2": float(np.linalg.norm(E_to_zero, 2) / (a * a)),
            "det_after_boundary_perturbation": float(np.linalg.det(M_zero)),
            "det_after_1pct_larger_perturbation": float(np.linalg.det(M_flip)),
        })

    GA = gram(A)
    GB = gram(B)
    n = GA.shape[0]
    pA = power_sums(GA, n)
    pB = power_sums(GB, n)
    eA = elementary_from_power(pA, n)
    eB = elementary_from_power(pB, n)

    global_rows = []
    for k in range(1, n + 1):
        global_rows.append({
            "order_k": k,
            "power_sum_A": pA[k],
            "power_sum_B": pB[k],
            "delta_power_sum": abs(pA[k] - pB[k]),
            "elementary_A": eA[k],
            "elementary_B": eB[k],
            "delta_elementary": abs(eA[k] - eB[k]),
        })

    detA = float(np.linalg.det(GA))
    detB = float(np.linalg.det(GB))

    result = {
        "gate": "gate9-algebraic-escape-audit",
        "status": "exact_algebraic_jump_exists_but_is_not_a_free_low_bandwidth_invariant",
        "local_pair_block": {
            "toy": "u(a)=[1,1+i a], H=u u^T + conj(u) conj(u)^T",
            "exact_formula": "det H(a) = -4 a^2",
            "rows": local_rows,
        },
        "homometric_global_gram": {
            "theta": THETA,
            "set_A": A.astype(int).tolist(),
            "set_B": B.astype(int).tolist(),
            "newton_identity_note": "e_k is determined by tr(G^j), j<=k; e_n=det(G)",
            "rows": global_rows,
            "det_A_direct": detA,
            "det_B_direct": detB,
            "det_A_from_e_n": eA[n],
            "det_B_from_e_n": eB[n],
        },
        "registered_checks": {
            "P9A_local_determinant_is_minus4a2": all(
                abs(r["det_over_minus4a2"] - 1.0) < 1e-8 for r in local_rows
            ),
            "P9B_rank_boundary_operator_error_is_quadratic": abs(
                local_rows[-1]["error_to_boundary_over_a2"] - 1.0
            ) < 1e-6,
            "P9C_one_percent_extra_error_can_flip_determinant_sign": all(
                r["det_after_1pct_larger_perturbation"] > 0.0 for r in local_rows
            ),
            "P9D_e1_e2_homometric_tie": (
                global_rows[0]["delta_elementary"] < 1e-10
                and global_rows[1]["delta_elementary"] < 1e-10
            ),
            "P9E_e3_escapes_pair_tie": global_rows[2]["delta_elementary"] > 1e-5,
            "P9F_full_determinant_is_top_elementary_invariant": (
                abs(detA - eA[n]) < 1e-10 and abs(detB - eB[n]) < 1e-10
            ),
        },
    }
    result["all_registered_checks_pass"] = all(result["registered_checks"].values())

    out = OUT / "gate9_algebraic_escape_audit.json"
    out.write_text(json.dumps(result, indent=2), encoding="utf-8")

    print("Gate 9 — algebraic escape audit")
    print("================================")
    print("local det/a^2:", [(r["a"], r["det_over_minus4a2"]) for r in local_rows])
    print("local rank-boundary / a^2:",
          [(r["a"], r["error_to_boundary_over_a2"]) for r in local_rows])
    print("elementary deltas:",
          [(r["order_k"], r["delta_elementary"]) for r in global_rows])
    print("direct det delta:", abs(detA - detB))
    print("all registered checks:", result["all_registered_checks_pass"])
    print("wrote", out)


if __name__ == "__main__":
    main()
