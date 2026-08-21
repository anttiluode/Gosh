#!/usr/bin/env python3
"""
Gate 5 — bandlimit the L2 pair idea and attack what remains.

No RH claim. This script checks only the analytic toy statements used by the note.

P5A  The compact-Fourier truncation of K_eta obeys the explicit strip tail bound
     at representative complex points.
P5B  The dimensionless tail scale is 2(x+1)e^{-x}, x=2*pi*(eta-d)*B.
P5C  After center averaging, the resulting autocorrelation is a translation-
     invariant pair kernel and therefore ties on the Gate-1 homometric attacker.

Dependency: numpy.
"""

import json
import math
from pathlib import Path

import numpy as np

OUT = Path("results")
OUT.mkdir(exist_ok=True)
PI = math.pi

A = np.array([0, 1, 4, 10, 12, 17], dtype=float)
BSET = np.array([0, 1, 8, 11, 13, 17], dtype=float)


def K_full(z: complex, eta: float) -> complex:
    return 1.0 / (z - 1j * eta) ** 2 + 1.0 / (z + 1j * eta) ** 2


def K_bandlimited(z: complex, eta: float, bandwidth: float, n: int = 50001) -> complex:
    xi = np.linspace(-bandwidth, bandwidth, n)
    hat = -4.0 * PI**2 * np.abs(xi) * np.exp(-2.0 * PI * eta * np.abs(xi))
    values = hat * np.exp(2j * PI * xi * z)
    return complex(np.trapezoid(values, xi))


def strip_tail_bound(eta: float, d: float, bandwidth: float) -> float:
    margin = eta - d
    if margin <= 0:
        return math.inf
    alpha = 2.0 * PI * margin
    return 8.0 * PI**2 * math.exp(-alpha * bandwidth) * (
        bandwidth / alpha + 1.0 / alpha**2
    )


def dimensionless_tail_bound(x: float) -> float:
    return 2.0 * (x + 1.0) * math.exp(-x)


def autocorr_kernel(delta: float, eta: float, bandwidth: float, n: int = 10001) -> float:
    """Autocorrelation of the bandlimited atom; depends only on the difference."""
    xi = np.linspace(0.0, bandwidth, n)
    atom_hat_sq = (
        4.0 * PI**2 * xi * np.exp(-2.0 * PI * eta * xi)
    ) ** 2
    return float(
        2.0
        * np.trapezoid(
            atom_hat_sq * np.cos(2.0 * PI * xi * delta),
            xi,
        )
    )


def pair_score(points: np.ndarray, eta: float, bandwidth: float) -> float:
    diffs = (points[:, None] - points[None, :]).ravel()
    unique = np.unique(diffs)
    kernel = {
        float(d): autocorr_kernel(float(d), eta, bandwidth) for d in unique
    }
    return float(sum(kernel[float(d)] for d in diffs))


def main():
    complex_checks = []
    for z, eta, bandwidth in [
        (1.2 + 0.3j, 0.5, 2.0),
        (0.7 + 0.1j, 0.5, 2.0),
        (1.2 + 0.3j, 0.5, 4.0),
        (0.5 + 0.4j, 0.5, 4.0),
    ]:
        exact = K_full(z, eta)
        trunc = K_bandlimited(z, eta, bandwidth)
        error = abs(exact - trunc)
        bound = strip_tail_bound(eta, abs(z.imag), bandwidth)
        complex_checks.append(
            {
                "z_real": z.real,
                "z_imag": z.imag,
                "eta": eta,
                "bandwidth": bandwidth,
                "abs_error": error,
                "tail_bound": bound,
                "error_over_bound": error / bound,
                "bound_holds": error <= bound,
            }
        )

    horizon_rows = [
        {"x": x, "scaled_tail_bound": dimensionless_tail_bound(x)}
        for x in [0.1, 0.5, 1.0, 2.0, 4.0, 8.0, 12.0]
    ]

    pair_rows = []
    for eta, bandwidth in [
        (0.5, 0.5),
        (0.5, 1.0),
        (0.5, 2.0),
        (0.75, 1.0),
        (0.75, 2.0),
    ]:
        score_a = pair_score(A, eta, bandwidth)
        score_b = pair_score(BSET, eta, bandwidth)
        pair_rows.append(
            {
                "eta": eta,
                "bandwidth": bandwidth,
                "score_A": score_a,
                "score_B": score_b,
                "abs_difference": abs(score_a - score_b),
            }
        )

    result = {
        "gate": "gate5-bandlimited-l2",
        "status": "admissibility_possible_pair_projection_is_blind",
        "kernel": {
            "K_eta": "1/(u-i*eta)^2 + 1/(u+i*eta)^2",
            "fourier": "-4*pi^2*|xi|*exp(-2*pi*eta*|xi|)",
            "strip_tail_bound": "8*pi^2*exp(-alpha*B)*(B/alpha+1/alpha^2), alpha=2*pi*(eta-d)",
            "scaled_tail_bound": "2*(x+1)*exp(-x), x=2*pi*(eta-d)*B",
        },
        "complex_tail_checks": complex_checks,
        "dimensionless_horizon": horizon_rows,
        "homometric_pair_autocorrelation_checks": pair_rows,
        "registered_checks": {
            "P5A_tail_bounds_hold": all(r["bound_holds"] for r in complex_checks),
            "P5B_tail_decreases_after_x1": all(
                horizon_rows[i + 1]["scaled_tail_bound"]
                < horizon_rows[i]["scaled_tail_bound"]
                for i in range(2, len(horizon_rows) - 1)
            ),
            "P5C_pair_projection_homometric_tie": all(
                r["abs_difference"] < 1e-10 for r in pair_rows
            ),
        },
    }
    result["all_registered_checks_pass"] = all(result["registered_checks"].values())

    out = OUT / "gate5_bandlimited_l2.json"
    out.write_text(json.dumps(result, indent=2), encoding="utf-8")

    print("Gate 5 — bandlimited L2")
    print("========================")
    print("max error/bound:", max(r["error_over_bound"] for r in complex_checks))
    print("horizon:", [(r["x"], r["scaled_tail_bound"]) for r in horizon_rows])
    print("pair differences:", [r["abs_difference"] for r in pair_rows])
    print("all registered checks:", result["all_registered_checks_pass"])
    print("wrote", out)


if __name__ == "__main__":
    main()
