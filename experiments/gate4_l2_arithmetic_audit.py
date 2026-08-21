#!/usr/bin/env python3
"""
Gate 4 — L2 arithmetic audit

Structure/falsification experiment only. No RH claim.

Checks:
P4A  The transverse y^4 coefficient L2 agrees with the exact pair identity
      L2/f^2 = sum_{j<k} [(t-z_j)^-2 (t-z_k)^-2]
      for a real-root polynomial.
P4B  The normalized pair statistic has a second-order pole near a simple zero
      while L2 itself stays finite.
P4C  With Gate-2 large legs fixed, unequal connector legs beat equal ones.
P4D  On a matched scaled grid, doubling the total aperture keeps the best
      small-leg absolute budget at 0.20 rather than preserving its fraction.

Dependency: numpy.
"""

import json
from pathlib import Path
import numpy as np

OUT = Path("results")
OUT.mkdir(exist_ok=True)


# ---------------------------------------------------------------------------
# 1. L2 pair identity on a canonical finite product
# ---------------------------------------------------------------------------
ROOTS = np.array([-3.0, -1.0, 2.0, 4.0])
P = np.poly1d(np.poly(ROOTS))
P1 = np.polyder(P, 1)
P2 = np.polyder(P, 2)
P3 = np.polyder(P, 3)
P4 = np.polyder(P, 4)


def L2_derivative_form(t):
    f = P(t)
    return f * P4(t) / 12.0 - P1(t) * P3(t) / 3.0 + P2(t) ** 2 / 4.0


def normalized_pair_form(t):
    q = [1.0 / (t - r) ** 2 for r in ROOTS]
    return sum(q[i] * q[j] for i in range(len(q)) for j in range(i + 1, len(q)))


# ---------------------------------------------------------------------------
# 2. Gate-2 mixed-aperture attacker
# ---------------------------------------------------------------------------
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


def search_allocations(total, step, max_theta):
    units = int(round(total / step))
    max_units = int(round(max_theta / step))
    best = None
    count = 0

    for u1 in range(1, min(max_units, units - 3) + 1):
        for u2 in range(1, min(max_units, units - u1 - 2) + 1):
            for u3 in range(1, min(max_units, units - u1 - u2 - 1) + 1):
                u4 = units - u1 - u2 - u3
                if u4 < 1 or u4 > max_units:
                    continue
                t = tuple(step * u for u in (u1, u2, u3, u4))
                s = separation(t)
                count += 1
                if best is None or s > best["abs_separation"]:
                    best = {"thetas": list(t), "abs_separation": s}
    best["configurations_checked"] = count
    return best


def two_smallest_sum(thetas):
    vals = sorted(thetas)
    return vals[0] + vals[1]


def main():
    identity_rows = []
    for t in [0.3, 1.1, 5.0]:
        l2 = float(L2_derivative_form(t))
        f2pair = float(P(t) ** 2 * normalized_pair_form(t))
        identity_rows.append({
            "t": t,
            "L2_derivative_form": l2,
            "f2_times_pair_form": f2pair,
            "abs_error": abs(l2 - f2pair),
        })

    # Near the simple zero r0=-1, the coefficient of eps^-2 is
    # sum_{k!=j} 1/(r_j-r_k)^2.
    r0 = -1.0
    pole_constant = float(sum(1.0 / (r0 - r) ** 2 for r in ROOTS if r != r0))
    singular_rows = []
    for eps in [1e-1, 1e-2, 1e-3, 1e-4]:
        t = r0 + eps
        h = float(L2_derivative_form(t) / (P(t) ** 2))
        singular_rows.append({
            "eps": eps,
            "normalized_L2": h,
            "eps2_times_normalized_L2": h * eps * eps,
            "regular_L2": float(L2_derivative_form(t)),
        })

    fixed_large_asym = (0.70, 0.05, 0.70, 0.15)
    fixed_large_equal = (0.70, 0.10, 0.70, 0.10)

    best_16 = search_allocations(total=1.6, step=0.05, max_theta=1.0)
    best_32 = search_allocations(total=3.2, step=0.10, max_theta=2.0)

    small16 = two_smallest_sum(best_16["thetas"])
    small32 = two_smallest_sum(best_32["thetas"])

    result = {
        "gate": "gate4-l2-arithmetic-audit",
        "status": "algebraic_two_level_yes_arithmetic_admissibility_open",
        "L2_pair_identity": {
            "formula": "L2/f^2 = sum_{j<k} 1/((t-z_j)^2 (t-z_k)^2)",
            "roots": ROOTS.tolist(),
            "rows": identity_rows,
        },
        "normalized_singularity": {
            "simple_zero": r0,
            "predicted_eps_minus2_coefficient": pole_constant,
            "rows": singular_rows,
        },
        "gate2_connector_tests": {
            "fixed_large_legs": {
                "asymmetric": {
                    "thetas": list(fixed_large_asym),
                    "abs_separation": separation(fixed_large_asym),
                },
                "equal_small_legs": {
                    "thetas": list(fixed_large_equal),
                    "abs_separation": separation(fixed_large_equal),
                },
            },
            "matched_scaled_grid": {
                "total_1_6": best_16,
                "small_leg_sum_1_6": small16,
                "small_leg_fraction_1_6": small16 / 1.6,
                "total_3_2": best_32,
                "small_leg_sum_3_2": small32,
                "small_leg_fraction_3_2": small32 / 3.2,
            },
        },
        "registered_checks": {
            "P4A_pair_identity": all(r["abs_error"] < 1e-10 for r in identity_rows),
            "P4B_normalized_has_eps_minus2_pole": abs(singular_rows[-1]["eps2_times_normalized_L2"] - pole_constant) < 1e-3,
            "P4B_regular_L2_stays_finite": abs(singular_rows[-1]["regular_L2"]) < 1e4,
            "P4C_unequal_small_legs_win_at_fixed_large": separation(fixed_large_asym) > separation(fixed_large_equal),
            "P4D_absolute_small_budget_beats_ratio_story_on_matched_grid": abs(small16 - small32) < 1e-12 and (small32 / 3.2) < (small16 / 1.6),
        },
    }
    result["all_registered_checks_pass"] = all(result["registered_checks"].values())

    out = OUT / "gate4_l2_arithmetic_audit.json"
    out.write_text(json.dumps(result, indent=2), encoding="utf-8")

    print("Gate 4 — L2 arithmetic audit")
    print("==========================")
    print("pair identity max error:", max(r["abs_error"] for r in identity_rows))
    print("predicted pole coefficient:", pole_constant)
    print("eps^2 * normalized L2 at 1e-4:", singular_rows[-1]["eps2_times_normalized_L2"])
    print("asym/equal connector separation:", separation(fixed_large_asym), separation(fixed_large_equal))
    print("1.6 best:", best_16)
    print("3.2 best:", best_32)
    print("all registered checks:", result["all_registered_checks_pass"])
    print("wrote", out)


if __name__ == "__main__":
    main()
