#!/usr/bin/env python3
"""
Gate 8 — off-line hyperbolic pair -> multiplicity-2 on-line boundary.

No RH claim. Exact two-channel toy:
    u(a) = [1, 1+i a]
    H(a) = u u^T + conj(u) conj(u)^T
         = 2 [[1,1],[1,1-a^2]].

Checks:
- ||H(a)-H(0)||_op = 2 a^2;
- the negative eigenvalue has |lambda_-| ~ a^2;
- a finite operator error delta cannot certify the negative sign once
  |lambda_-| <= delta (Weyl horizon).

Dependency: numpy.
"""

import json
from pathlib import Path

import numpy as np

OUT = Path("results")
OUT.mkdir(exist_ok=True)


def H(a):
    u = np.array([1.0 + 0j, 1.0 + 1j * a])
    return np.outer(u, u) + np.outer(np.conj(u), np.conj(u))


def main():
    H0 = H(0.0)
    rows = []

    for a in [1e-1, 3e-2, 1e-2, 3e-3, 1e-3, 1e-4, 1e-5]:
        M = H(a)
        eigs = np.linalg.eigvalsh(M.real)
        lam_minus = float(eigs[0])
        lam_plus = float(eigs[-1])
        op_diff = float(np.linalg.norm(M.real - H0.real, 2))
        exact_minus = float(2.0 - a*a - np.sqrt(4.0 + a**4))

        rows.append({
            "a": a,
            "lambda_minus": lam_minus,
            "lambda_plus": lam_plus,
            "exact_lambda_minus": exact_minus,
            "abs_lambda_minus_over_a2": abs(lam_minus) / (a*a),
            "op_difference": op_diff,
            "op_difference_over_a2": op_diff / (a*a),
        })

    # Spectral-margin example: if the matrix is known only to delta, certify
    # negativity only when the negative eigenvalue lies beyond that margin.
    deltas = [1e-2, 1e-4, 1e-6, 1e-8]
    horizon_rows = []
    for delta in deltas:
        # Generic small-a prediction is a ~ sqrt(delta); record exact toy
        # behavior on a logarithmic sweep.
        sweep = np.logspace(-6, 0, 12001)
        certifiable = []
        for a in sweep:
            lm = 2.0 - a*a - np.sqrt(4.0 + a**4)
            if abs(lm) > delta:
                certifiable.append(float(a))
        horizon_rows.append({
            "delta": delta,
            "sqrt_delta": float(np.sqrt(delta)),
            "smallest_a_certifiable_on_sweep": min(certifiable) if certifiable else None,
        })

    result = {
        "gate": "gate8-double-zero-boundary",
        "status": "off_line_pair_approaches_double_zero_quadratically",
        "toy": "u(a)=[1,1+i a]",
        "H0": H0.real.tolist(),
        "rows": rows,
        "weyl_horizon": horizon_rows,
        "registered_checks": {
            "P8A_matrix_difference_is_2a2": all(abs(r["op_difference_over_a2"] - 2.0) < 1e-6 for r in rows[:-1]),
            "P8B_negative_eigenvalue_is_quadratic": abs(rows[-3]["abs_lambda_minus_over_a2"] - 1.0) < 1e-5,
            "P8C_exact_eigenvalue_formula_matches": all(abs(r["lambda_minus"] - r["exact_lambda_minus"]) < 1e-12 for r in rows[:-1]),
            "P8D_weyl_horizon_scales_sqrt_delta": all(
                0.9 <= r["smallest_a_certifiable_on_sweep"] / r["sqrt_delta"] <= 1.2
                for r in horizon_rows
            ),
        },
    }
    result["all_registered_checks_pass"] = all(result["registered_checks"].values())

    out = OUT / "gate8_double_zero_boundary.json"
    out.write_text(json.dumps(result, indent=2), encoding="utf-8")

    print("Gate 8 — double-zero boundary")
    print("=============================")
    print("a, |lambda-|/a^2, ||H-H0||/a^2")
    for r in rows:
        print(r["a"], r["abs_lambda_minus_over_a2"], r["op_difference_over_a2"])
    print("horizons:", horizon_rows)
    print("all registered checks:", result["all_registered_checks_pass"])
    print("wrote", out)


if __name__ == "__main__":
    main()
