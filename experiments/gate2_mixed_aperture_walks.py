#!/usr/bin/env python3
"""
Gate 2 — Mixed-aperture closed walks under a fixed toy support budget

Information toy only. No zeta theorem is asserted.

We continue with the non-congruent homometric pair
    A = {0,1,4,10,12,17}
    B = {0,1,8,11,13,17}.

For each aperture theta define the translation-invariant sinc Gram matrix
    G_theta(x)_{ij} = sinc(theta * (x_i-x_j)).

A two-leg mixed trace
    tr(G_a G_b)
still depends only on pairwise distances, so homometry forces a tie for ANY
(a,b). For 3+ legs, the product is a genuinely closed-walk statistic and can
see how the same edges are assembled.

The AnttisBrain-shaped experiment allocates a FIXED total toy support budget S
across the legs of a fourth-order mixed trace
    tr(G_t1 G_t2 G_t3 G_t4).
It compares equal allocation with an exhaustive discrete asymmetric allocation.

This is deliberately NOT presented as the arithmetic support theorem used in
n-level correlation. 'sum theta = S' is a toy budget used to test the
information geometry of resolution allocation.

Registered predictions
----------------------
P2A: mixed two-leg traces tie for the homometric pair at representative unequal apertures.
P2B: a fourth-order mixed trace separates the pair under total budget S=1.6.
P2C: some asymmetric allocation with each theta <= 1 improves separation over
     equal allocation (0.4,0.4,0.4,0.4).
"""

import json
from pathlib import Path

import numpy as np


OUT = Path("results")
OUT.mkdir(exist_ok=True)

A = np.array([0, 1, 4, 10, 12, 17], dtype=float)
B = np.array([0, 1, 8, 11, 13, 17], dtype=float)


def gram(x, theta):
    d = x[:, None] - x[None, :]
    return np.sinc(theta * d)


def mixed_trace(x, thetas):
    M = np.eye(len(x))
    for theta in thetas:
        M = M @ gram(x, theta)
    return float(np.trace(M))


def separation(thetas):
    return abs(mixed_trace(A, thetas) - mixed_trace(B, thetas))


def search_allocations(total=1.6, step=0.05, max_theta=1.0):
    units = int(round(total / step))
    max_units = int(round(max_theta / step))
    rows = []

    for u1 in range(1, min(max_units, units - 3) + 1):
        for u2 in range(1, min(max_units, units - u1 - 2) + 1):
            for u3 in range(1, min(max_units, units - u1 - u2 - 1) + 1):
                u4 = units - u1 - u2 - u3
                if u4 < 1 or u4 > max_units:
                    continue
                thetas = tuple(step * u for u in (u1, u2, u3, u4))
                ta = mixed_trace(A, thetas)
                tb = mixed_trace(B, thetas)
                rows.append({
                    "thetas": list(thetas),
                    "trace_A": ta,
                    "trace_B": tb,
                    "abs_separation": abs(ta - tb),
                })

    rows.sort(key=lambda r: r["abs_separation"], reverse=True)
    return rows


def main():
    pair_checks = []
    for thetas in [(0.8, 0.8), (1.0, 0.6), (0.7, 0.1), (0.4, 0.4), (0.95, 0.05)]:
        pair_checks.append({
            "thetas": list(thetas),
            "abs_separation": separation(thetas),
        })

    pair_tie = all(r["abs_separation"] < 1e-10 for r in pair_checks)

    total = 1.6
    equal = (0.4, 0.4, 0.4, 0.4)
    equal_A = mixed_trace(A, equal)
    equal_B = mixed_trace(B, equal)
    equal_sep = abs(equal_A - equal_B)

    rows = search_allocations(total=total, step=0.05, max_theta=1.0)
    best = rows[0]
    gain = best["abs_separation"] / equal_sep

    result = {
        "gate": "gate2-mixed-aperture-walks",
        "status": "information_toy_not_an_arithmetic_support_theorem",
        "set_A": A.astype(int).tolist(),
        "set_B": B.astype(int).tolist(),
        "two_leg_mixed_trace_checks": pair_checks,
        "fixed_total_toy_support": total,
        "allocation_step": 0.05,
        "per_leg_max_theta": 1.0,
        "equal_allocation": {
            "thetas": list(equal),
            "trace_A": equal_A,
            "trace_B": equal_B,
            "abs_separation": equal_sep,
        },
        "best_asymmetric_allocation": best,
        "separation_gain_over_equal": gain,
        "top_10_allocations": rows[:10],
        "P2A_two_leg_pair_statistics_tie": pair_tie,
        "P2B_four_leg_mixed_trace_separates": equal_sep > 1e-4,
        "P2C_asymmetric_allocation_improves": best["abs_separation"] > equal_sep + 1e-4,
    }
    result["all_registered_predictions_pass"] = all([
        result["P2A_two_leg_pair_statistics_tie"],
        result["P2B_four_leg_mixed_trace_separates"],
        result["P2C_asymmetric_allocation_improves"],
    ])

    out = OUT / "gate2_mixed_aperture_walks.json"
    out.write_text(json.dumps(result, indent=2), encoding="utf-8")

    print("Gate 2 — mixed-aperture closed walks")
    print("====================================")
    print("two-leg mixed traces tied:", pair_tie)
    print("equal allocation", equal, "separation", equal_sep)
    print("best allocation", best["thetas"], "separation", best["abs_separation"])
    print("gain over equal:", gain)
    print("all registered predictions:", result["all_registered_predictions_pass"])
    print("wrote", out)


if __name__ == "__main__":
    main()
