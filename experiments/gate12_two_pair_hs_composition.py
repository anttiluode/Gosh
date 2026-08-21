#!/usr/bin/env python3
"""
Gate 12 — two-pair Hilbert-Schmidt composition.

For full-lattice reflected pair blocks H_i and their virtual on-line doubles
V_i, Gate 11 gives an analytic overlap kernel k. Put f=k^2. Since k is
positive definite on R, f is positive definite and has a nonnegative even
Bochner measure mu.

For pair center x_i and transverse depth D_i one gets exactly

  ||sum_i H_i||_HS^2
    = 4 int |sum_i cosh(2*pi*xi*D_i) exp(2*pi*i*xi*x_i)|^2 dmu(xi),

  ||sum_i V_i||_HS^2
    = 4 int |sum_i exp(2*pi*i*xi*x_i)|^2 dmu(xi).

Consequences:
  * common depth D, any number of pairs: actual HS >= virtual HS pointwise;
  * two pairs, arbitrary D1,D2: actual HS >= virtual HS pointwise because
      c1^2+c2^2-2+2(c1*c2-1)cos(theta) >= (c1-c2)^2 >= 0;
  * three unequal depths are the first place the pointwise argument can fail.

This does not prove the nonlinear stability-defect bridge. It shows that the
public certified two-pair failure of additive local bridge pricing is not a
failure of the raw second-moment/Hilbert-Schmidt composition.

The numerical checks below use the Montgomery-Taylor limiting kernel.
"""

import json
import math
import cmath
from pathlib import Path

import numpy as np

OUT = Path("results")
OUT.mkdir(exist_ok=True)

PI = math.pi
C = 1.0 / math.sqrt(2.0)
K0 = math.sqrt(2.0) * math.sin(C)


def sinc(z):
    if abs(z) < 1e-14:
        return 1.0 + 0.0j
    return cmath.sin(PI * z) / (PI * z)


def k(z):
    return 0.5 * (sinc(z - C / PI) + sinc(z + C / PI)) / K0


def f(z):
    return k(z) ** 2


def pair_cross(dx, Di, Dj):
    """tr(H_i H_j) from the exact complex-kernel formula."""
    return 2.0 * (
        f(dx - 1j * (Di - Dj)) + f(dx - 1j * (Di + Dj))
    ).real


def hs_diff(xs, Ds):
    """||sum H_i||_HS^2 - ||sum V_i||_HS^2."""
    actual = 0.0
    virtual = 0.0
    for i in range(len(xs)):
        for j in range(len(xs)):
            dx = xs[i] - xs[j]
            actual += pair_cross(dx, Ds[i], Ds[j])
            virtual += 4.0 * f(dx).real
    return actual - virtual


def two_weight_pointwise(c1, c2, theta):
    return c1*c1 + c2*c2 - 2.0 + 2.0 * (c1*c2 - 1.0) * math.cos(theta)


def main():
    rng = np.random.default_rng(42)

    two_rows = []
    min_two = float("inf")
    for _ in range(20000):
        x = float(rng.uniform(0.0, 12.0))
        D1 = float(rng.uniform(0.0, 1.5))
        D2 = float(rng.uniform(0.0, 1.5))
        diff = hs_diff([0.0, x], [D1, D2])
        min_two = min(min_two, diff)
        if len(two_rows) < 12:
            two_rows.append({"x": x, "D1": D1, "D2": D2, "hs_actual_minus_virtual": diff})

    equal_rows = []
    min_equal = float("inf")
    for _ in range(5000):
        m = int(rng.integers(2, 9))
        xs = np.sort(rng.uniform(0.0, 10.0, m)).tolist()
        D = float(rng.uniform(0.0, 1.0))
        diff = hs_diff(xs, [D] * m)
        min_equal = min(min_equal, diff)
        if len(equal_rows) < 12:
            equal_rows.append({"m": m, "D": D, "xs": xs, "hs_actual_minus_virtual": diff})

    # Algebraic frequency-level obstruction to extending the two-weight proof
    # to three arbitrary unequal weights. All weights exceed 1.
    c3 = [1.01, 1.01, 2.0]
    phases = [0.0, 0.0, math.pi]
    unweighted = abs(sum(cmath.exp(1j*p) for p in phases)) ** 2
    weighted = abs(sum(c*cmath.exp(1j*p) for c, p in zip(c3, phases))) ** 2
    three_point_integrand_difference = weighted - unweighted

    # Directly audit the pointwise two-weight inequality over random values.
    min_two_pointwise = float("inf")
    for _ in range(50000):
        c1 = 1.0 + float(rng.exponential(2.0))
        c2 = 1.0 + float(rng.exponential(2.0))
        theta = float(rng.uniform(-math.pi, math.pi))
        min_two_pointwise = min(min_two_pointwise, two_weight_pointwise(c1, c2, theta))

    result = {
        "gate": "gate12-two-pair-hs-composition",
        "status": "raw_second_moment_composes_for_two_pairs_and_common_depth_families",
        "exact_formula": {
            "actual": "4 int |sum_i cosh(2*pi*xi*D_i) exp(2*pi*i*xi*x_i)|^2 dmu(xi)",
            "virtual": "4 int |sum_i exp(2*pi*i*xi*x_i)|^2 dmu(xi)",
            "mu": "Bochner measure of f=k^2, nonnegative because k is positive definite",
        },
        "theorems": {
            "common_depth_any_m": "actual HS >= virtual HS pointwise in frequency",
            "two_pairs_arbitrary_depths": "actual HS >= virtual HS pointwise in frequency",
            "two_pair_minimum_identity": "min_theta difference = (c1-c2)^2 >= 0",
            "three_unequal_weights": "pointwise monotonicity can fail; positivity alone no longer proves composition"
        },
        "montgomery_taylor_random_audit": {
            "two_pair_samples": 20000,
            "minimum_two_pair_hs_difference": min_two,
            "sample_rows": two_rows,
            "common_depth_samples": 5000,
            "minimum_common_depth_hs_difference": min_equal,
            "common_depth_sample_rows": equal_rows,
        },
        "frequency_level_three_weight_obstruction": {
            "weights": c3,
            "phases": phases,
            "unweighted_modulus_sq": unweighted,
            "weighted_modulus_sq": weighted,
            "difference": three_point_integrand_difference,
        },
        "registered_checks": {
            "P12A_two_pair_random_sweep_nonnegative": min_two >= -1e-9,
            "P12B_common_depth_random_sweep_nonnegative": min_equal >= -1e-9,
            "P12C_two_weight_pointwise_sweep_nonnegative": min_two_pointwise >= -1e-12,
            "P12D_three_unequal_weight_pointwise_extension_fails": three_point_integrand_difference < -0.9,
        },
    }
    result["all_registered_checks_pass"] = all(result["registered_checks"].values())

    out = OUT / "gate12_two_pair_hs_composition.json"
    out.write_text(json.dumps(result, indent=2), encoding="utf-8")

    print("Gate 12 — two-pair HS composition")
    print("=================================")
    print("min two-pair MT sweep:", min_two)
    print("min common-depth MT sweep:", min_equal)
    print("min pointwise two-weight sweep:", min_two_pointwise)
    print("three-weight pointwise obstruction:", three_point_integrand_difference)
    print("all registered checks:", result["all_registered_checks_pass"])
    print("wrote", out)


if __name__ == "__main__":
    main()
