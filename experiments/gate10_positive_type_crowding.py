#!/usr/bin/env python3
"""
Gate 10 — positive-type crowding audit.

A public follow-up campaign suggests that the remaining off-line-pair bridge
might require a Szego/Ingham-style "anti-crowding" statement for Gram matrices
of translates of the actual positive-type bandlimited overlap kernel.

This gate tests the weakest possible version of that hope on the optimized
Montgomery-Taylor kernel used by the 2026 framework.

Result preview:
positive type alone does NOT keep Gram eigenvalues away from the spectral
threshold 2. Two arbitrarily close translates have eigenvalues 1 +/- k(d),
so the upper eigenvalue approaches 2 quadratically as d -> 0. Larger clusters
approach the all-ones Gram matrix.

No RH claim. This does not refute a more structured bridge theorem; it says
such a theorem must use more than Bochner positivity alone (for example a
spacing/density pressure term, configuration averaging, or a special defect
identity).

Dependency: numpy.
"""

import json
import math
from pathlib import Path

import numpy as np

OUT = Path("results")
OUT.mkdir(exist_ok=True)

PI = math.pi
C = 1.0 / math.sqrt(2.0)
K0 = math.sqrt(2.0) * math.sin(C)


def K(x):
    """Entire overlap kernel in a numerically stable sinc form."""
    x = np.asarray(x, dtype=float)
    return 0.5 * (np.sinc(x - C / PI) + np.sinc(x + C / PI))


def k(x):
    """Normalize so k(0)=1."""
    return K(x) / K0


def spectral_second_moment(n=200001):
    """E[t^2] for spectral density cos(sqrt(2)t) on [-1/2,1/2]."""
    t = np.linspace(-0.5, 0.5, n)
    w = np.cos(math.sqrt(2.0) * t)
    return float(np.trapezoid(w * t * t, t) / np.trapezoid(w, t))


def gram(points):
    points = np.asarray(points, dtype=float)
    d = points[:, None] - points[None, :]
    return k(d)


def psi(x):
    x = np.asarray(x, dtype=float)
    return np.where(x <= 2.0, (x - 1.0) ** 2, 2.0 * x - 3.0)


def main():
    et2 = spectral_second_moment()
    quadratic_coefficient = 2.0 * PI**2 * et2

    pair_rows = []
    for d in [1e-1, 3e-2, 1e-2, 3e-3, 1e-3, 3e-4, 1e-4]:
        kd = float(k(d))
        G = np.array([[1.0, kd], [kd, 1.0]])
        eigs = np.linalg.eigvalsh(G)
        lam_minus = float(eigs[0])
        lam_plus = float(eigs[1])
        pair_rows.append({
            "separation_d": d,
            "k_d": kd,
            "lambda_minus": lam_minus,
            "lambda_plus": lam_plus,
            "distance_lambda_plus_to_2": 2.0 - lam_plus,
            "distance_to_2_over_d2": (2.0 - lam_plus) / (d * d),
            "psi_trace": float(np.sum(psi(eigs))),
        })

    cluster_rows = []
    for m in [2, 3, 4, 6]:
        for eps in [0.1, 0.03, 0.01, 0.003]:
            points = np.arange(m, dtype=float) * eps
            eigs = np.linalg.eigvalsh(gram(points))
            cluster_rows.append({
                "points": m,
                "spacing_eps": eps,
                "smallest_eigenvalue": float(eigs[0]),
                "second_largest_eigenvalue": float(eigs[-2]) if m > 1 else None,
                "largest_eigenvalue": float(eigs[-1]),
                "largest_eigenvalue_distance_to_m": float(m - eigs[-1]),
                "psi_trace": float(np.sum(psi(eigs))),
            })

    result = {
        "gate": "gate10-positive-type-crowding",
        "status": "positive_type_alone_does_not_exclude_spectral_crowding",
        "kernel": {
            "name": "normalized Montgomery-Taylor overlap",
            "integral": "K(x)=int_{-1/2}^{1/2} cos(sqrt(2)t) cos(2*pi*x*t) dt",
            "stable_formula": "K(x)=0.5[sinc(x-c/pi)+sinc(x+c/pi)], c=1/sqrt(2)",
            "K0": K0,
            "spectral_density_positive_on_support": True,
            "spectral_second_moment": et2,
            "predicted_two_point_quadratic_coefficient": quadratic_coefficient,
        },
        "two_point_crowding": {
            "exact_eigenvalues": "1 +/- k(d)",
            "small_d_law": "2-lambda_plus = 1-k(d) = 2*pi^2*E[t^2]*d^2 + O(d^4)",
            "rows": pair_rows,
        },
        "multi_point_clusters": cluster_rows,
        "registered_checks": {
            "P10A_kernel_normalized": abs(float(k(0.0)) - 1.0) < 1e-14,
            "P10B_two_point_upper_eigenvalue_approaches_2": pair_rows[-1]["distance_lambda_plus_to_2"] < 2e-8,
            "P10C_quadratic_coefficient_matches_spectral_moment": abs(
                pair_rows[-1]["distance_to_2_over_d2"] / quadratic_coefficient - 1.0
            ) < 1e-6,
            "P10D_cluster_top_eigenvalue_approaches_cluster_size": all(
                r["largest_eigenvalue_distance_to_m"] < 0.01
                for r in cluster_rows
                if r["spacing_eps"] == 0.003
            ),
            "P10E_two_point_gram_is_psd": all(r["lambda_minus"] >= -1e-12 for r in pair_rows),
        },
    }
    result["all_registered_checks_pass"] = all(result["registered_checks"].values())

    out = OUT / "gate10_positive_type_crowding.json"
    out.write_text(json.dumps(result, indent=2), encoding="utf-8")

    print("Gate 10 — positive-type crowding audit")
    print("======================================")
    print("quadratic coefficient:", quadratic_coefficient)
    print("two-point ratios:",
          [(r["separation_d"], r["distance_to_2_over_d2"]) for r in pair_rows])
    print("cluster top eigenvalues at eps=.003:",
          [(r["points"], r["largest_eigenvalue"])
           for r in cluster_rows if r["spacing_eps"] == 0.003])
    print("all registered checks:", result["all_registered_checks_pass"])
    print("wrote", out)


if __name__ == "__main__":
    main()
