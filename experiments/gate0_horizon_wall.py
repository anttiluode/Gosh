#!/usr/bin/env python3
"""
Gate 0 — Moon Horizon vs. Riemann-style infinities

Purpose
-------
Test three sharply separated statements inspired by AnttisBrain2 / HorizonNet:

0A. A fixed-depth contraction horizon does NOT apply to the raw critical-line
    Dirichlet / prime amplitudes.
0B. A Neumann/Fredholm contraction horizon works away from a determinant zero,
    but its certified depth diverges as an eigenvalue approaches 1.
0C. A different horizon CAN certify a Hermitian decision (inertia): once a
    rigorous tail operator-norm bound is smaller than the spectral sign margin,
    Weyl perturbation guarantees that omitted terms cannot change inertia.

This is a toy gate. It does not compute Claude's Weil matrix and makes no claim
about RH.

Registered predictions
----------------------
P0A: term-magnitude ratios tend to 1, so no rho < 1 uniformly contracts the
     critical-line Dirichlet terms. A fixed four-term tail certificate fails.
P0B: for rho -> 1-, the Neumann depth needed for a fixed epsilon grows without
     bound; at rho >= 1 the geometric certificate is unavailable.
P0C: in the deterministic Hermitian toy series, there exists a finite K where
     tail_bound < spectral_margin, and from that K onward the inertia matches a
     long reference sum.
"""

import json
import math
from pathlib import Path

import numpy as np


OUT = Path("results")
OUT.mkdir(exist_ok=True)


def sieve(n: int):
    keep = np.ones(n + 1, dtype=bool)
    keep[:2] = False
    for p in range(2, int(n**0.5) + 1):
        if keep[p]:
            keep[p * p : n + 1 : p] = False
    return np.flatnonzero(keep)


def gate_0a():
    ns = np.array([10, 100, 1_000, 10_000, 1_000_000], dtype=float)
    # |(n+1)^(-1/2-it)| / |n^(-1/2-it)| = sqrt(n/(n+1))
    ratios = np.sqrt(ns / (ns + 1.0))

    ps = sieve(200_000)
    prime_abs_partial = np.cumsum(1.0 / np.sqrt(ps))
    checkpoints = [10, 100, 1_000, 10_000, 100_000, 200_000]
    prime_sums = {}
    for x in checkpoints:
        count = np.searchsorted(ps, x, side="right")
        prime_sums[str(x)] = float(prime_abs_partial[count - 1]) if count else 0.0

    # Rough Riemann-Siegel / approximate-functional-equation main-sum length.
    heights = [1e2, 1e4, 1e6, 1e12]
    rs_lengths = {f"{t:.0e}": int(math.floor(math.sqrt(t / (2.0 * math.pi))))
                  for t in heights}

    fixed_four_uniform_contraction = bool(np.max(ratios) < 0.99)

    return {
        "n_term_magnitude_ratios": {
            str(int(n)): float(r) for n, r in zip(ns, ratios)
        },
        "ratio_tends_to_one": True,
        "sum_p_inverse_sqrt_checkpoints": prime_sums,
        "rough_riemann_siegel_main_sum_lengths": rs_lengths,
        "fixed_four_uniform_contraction_below_0_99": fixed_four_uniform_contraction,
        "pass_prediction_P0A": (not fixed_four_uniform_contraction),
    }


def required_neumann_depth(rho: float, eps: float):
    """Smallest K with ||sum_{m>K} L^m|| <= rho^(K+1)/(1-rho) <= eps."""
    if rho >= 1.0:
        return None
    K = 0
    while rho ** (K + 1) / (1.0 - rho) > eps:
        K += 1
        if K > 10_000_000:
            raise RuntimeError("depth search runaway")
    return K


def gate_0b():
    eps = 1e-6
    rhos = [0.2, 0.5, 0.8, 0.9, 0.99, 0.999, 1.0]
    depths = {str(r): required_neumann_depth(r, eps) for r in rhos}

    # A literal 2x2 toy determinant: L_rho = diag(rho, 0.2).
    # det(I-L_rho)=(1-rho)(0.8), hence zero exactly at rho=1.
    determinants = {
        str(r): float((1.0 - r) * 0.8) for r in rhos
    }

    finite = [depths[str(r)] for r in rhos if r < 1]
    monotone = all(a < b for a, b in zip(finite, finite[1:]))
    zero_has_no_contraction_certificate = depths["1.0"] is None and determinants["1.0"] == 0.0

    return {
        "epsilon": eps,
        "rho_to_required_depth": depths,
        "rho_to_det_I_minus_L": determinants,
        "depths_strictly_increase_toward_one": monotone,
        "zero_at_rho_one_has_no_geometric_certificate": zero_has_no_contraction_certificate,
        "pass_prediction_P0B": monotone and zero_has_no_contraction_certificate,
    }


def toy_term(n: int):
    """
    Deterministic Hermitian rank-one term with ||term||_op = 1.
    The phases are deliberately incommensurate-ish, but carry NO zeta meaning.
    """
    u = np.array(
        [
            math.cos(0.7 * n),
            math.sin(0.7 * n),
            math.cos(1.3 * n),
            math.sin(1.3 * n),
        ],
        dtype=float,
    )
    u /= np.linalg.norm(u)
    sign = -1.0 if n % 3 == 0 else 1.0
    return sign * np.outer(u, u)


def inertia(eigs, tol=1e-12):
    neg = int(np.sum(eigs < -tol))
    zero = int(np.sum(np.abs(eigs) <= tol))
    pos = int(np.sum(eigs > tol))
    return [neg, zero, pos]


def gate_0c():
    # Infinite toy series:
    # G = G0 + sum_{n>=1} amp*q^(n-1) H_n, ||H_n||_op=1.
    # Hence omitted tail after K terms obeys
    # ||E_K||_op <= amp*q^K/(1-q).
    G0 = np.diag([-0.55, 0.35, 0.90, 1.40])
    amp = 0.40
    q = 0.60

    reference_terms = 200
    G_ref = G0.copy()
    for n in range(1, reference_terms + 1):
        G_ref += amp * q ** (n - 1) * toy_term(n)
    ref_eigs = np.linalg.eigvalsh(G_ref)
    ref_inertia = inertia(ref_eigs)

    rows = []
    first_certified = None
    for K in range(0, 21):
        GK = G0.copy()
        for n in range(1, K + 1):
            GK += amp * q ** (n - 1) * toy_term(n)
        eigs = np.linalg.eigvalsh(GK)
        margin = float(np.min(np.abs(eigs)))
        tail_bound = float(amp * q**K / (1.0 - q))
        certified = tail_bound < margin
        this_inertia = inertia(eigs)
        matches = this_inertia == ref_inertia

        if certified and first_certified is None:
            first_certified = K

        rows.append(
            {
                "K": K,
                "tail_op_bound": tail_bound,
                "spectral_sign_margin": margin,
                "certified_by_weyl": certified,
                "inertia": this_inertia,
                "matches_reference_inertia": matches,
            }
        )

    certified_rows = [r for r in rows if r["certified_by_weyl"]]
    all_certified_match = all(r["matches_reference_inertia"] for r in certified_rows)

    return {
        "amp": amp,
        "q": q,
        "reference_terms": reference_terms,
        "reference_eigenvalues": [float(x) for x in ref_eigs],
        "reference_inertia_neg_zero_pos": ref_inertia,
        "first_certified_K": first_certified,
        "rows": rows,
        "all_certified_rows_match_reference_inertia": all_certified_match,
        "pass_prediction_P0C": first_certified is not None and all_certified_match,
    }


def main():
    result = {
        "gate": "gate0-moon-horizon",
        "status": "toy_only_not_a_Riemann_result",
        "0A_raw_series": gate_0a(),
        "0B_neumann_zero_wall": gate_0b(),
        "0C_certificate_space_horizon": gate_0c(),
    }

    result["all_registered_predictions_pass"] = all(
        [
            result["0A_raw_series"]["pass_prediction_P0A"],
            result["0B_neumann_zero_wall"]["pass_prediction_P0B"],
            result["0C_certificate_space_horizon"]["pass_prediction_P0C"],
        ]
    )

    path = OUT / "gate0_horizon_wall.json"
    path.write_text(json.dumps(result, indent=2), encoding="utf-8")

    print("Gate 0 — Moon Horizon")
    print("=====================")
    print("0A raw critical-line series fixed-depth contraction:",
          "FAIL as predicted" if result["0A_raw_series"]["pass_prediction_P0A"] else "UNEXPECTED")
    print("0B contraction horizon at determinant zero:",
          "FAILS at zero as predicted" if result["0B_neumann_zero_wall"]["pass_prediction_P0B"] else "UNEXPECTED")
    print("0C certificate-space inertia horizon:",
          f"first certifies at K={result['0C_certificate_space_horizon']['first_certified_K']}")
    print("all registered predictions:", result["all_registered_predictions_pass"])
    print(f"wrote {path}")


if __name__ == "__main__":
    main()
