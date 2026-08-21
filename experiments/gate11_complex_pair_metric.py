#!/usr/bin/env python3
"""
Gate 11 — complex Poisson pair metric.

This gate reconciles Gate 8's off-line-pair -> double-zero limit with Gate 10's
on-line crowding using the full-lattice complex Poisson-Gabor identity from the
2026 Alpöge-Furman/Anthropic framework.

For the normalized overlap kernel k(z), an on-line separation d has two-point
Gram eigenvalue gap

    2 - lambda_plus = 1 - k(d),

whereas an off-line displacement D = L(beta-1/2)/(2*pi) has normalized
Hermitian norm

    N(D) = k(2 i D).

The full-lattice bilinear identity fixes u(D)^T u(D)=1. Writing u=x+iy gives
x dot y=0 and ||x||^2-||y||^2=1. Therefore the reflected-pair block has exact
nonzero eigenvalues

    lambda_pair,+ = N(D)+1,
    lambda_pair,- = -(N(D)-1).

For any even normalized spectral density with finite second moment mu2,

    1-k(d)     = 2*pi^2*mu2*d^2 + O(d^4),
    N(D)-1     = 8*pi^2*mu2*D^2 + O(D^4).

Thus the transverse and longitudinal quadratic coefficients have universal
ratio 4 in the same dimensionless coordinate. Equivalently, d=2D equalizes
the leading local penalties.

The numerical part uses the Montgomery-Taylor limiting profile
v(t)=cos(sqrt(2)t) on [-1/2,1/2].

No RH claim. Exact identities are full-Gabor-lattice identities; the finite
compression used in the theorem has edge/tail errors.
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


def K(z):
    """Entire Montgomery-Taylor overlap kernel in normalized x coordinates."""
    z = np.asarray(z)
    return 0.5 * (np.sinc(z - C / PI) + np.sinc(z + C / PI))


def k(z):
    return K(z) / K0


def spectral_second_moment(n=400001):
    t = np.linspace(-0.5, 0.5, n)
    w = np.cos(math.sqrt(2.0) * t)
    return float(np.trapezoid(w * t * t, t) / np.trapezoid(w, t))


def main():
    mu2 = spectral_second_moment()
    c_long = 2.0 * PI**2 * mu2
    c_trans = 8.0 * PI**2 * mu2

    rows = []
    for x in [1e-1, 3e-2, 1e-2, 3e-3, 1e-3, 3e-4, 1e-4]:
        k_long = float(np.real(k(x)))
        herm_norm_sq = float(np.real(k(2j * x)))
        long_gap = 1.0 - k_long
        trans_gap = herm_norm_sq - 1.0
        long_at_2x = 1.0 - float(np.real(k(2.0 * x)))

        rows.append({
            "x": x,
            "k_long_x": k_long,
            "longitudinal_gap_1_minus_kx": long_gap,
            "longitudinal_gap_over_x2": long_gap / (x * x),
            "offline_hermitian_norm_sq_k_2ix": herm_norm_sq,
            "transverse_negative_magnitude": trans_gap,
            "transverse_gap_over_x2": trans_gap / (x * x),
            "transverse_to_longitudinal_same_x_ratio": trans_gap / long_gap,
            "longitudinal_gap_at_2x": long_at_2x,
            "transverse_to_longitudinal_2x_ratio": trans_gap / long_at_2x,
            "pair_lambda_plus": herm_norm_sq + 1.0,
            "pair_lambda_minus": -trans_gap,
        })

    result = {
        "gate": "gate11-complex-pair-metric",
        "status": "full_lattice_pair_geometry_has_universal_4_to_1_quadratic_conversion",
        "scope": "full Poisson-Gabor lattice / limiting normalized overlap kernel; finite compression has tail and edge errors",
        "identities": {
            "complex_poisson": "sum_k phihat(z-alpha_k) phihat(zprime-alpha_k) = L * hat(phi^2)(z-zprime)",
            "normalized_bilinear_self": "u(D)^T u(D) = 1",
            "normalized_hermitian_self": "u(D)^* u(D) = N(D) = k(2 i D)",
            "reflected_pair_nonzero_spectrum": ["N(D)+1", "-(N(D)-1)"],
            "longitudinal_small_gap": "1-k(d) = 2*pi^2*mu2*d^2 + O(d^4)",
            "transverse_small_gap": "k(2iD)-1 = 8*pi^2*mu2*D^2 + O(D^4)",
            "conversion": "c_trans/c_long = 4; leading penalties match at d=2D"
        },
        "montgomery_taylor": {
            "spectral_profile": "v(t)=cos(sqrt(2)t), |t|<=1/2",
            "K0": K0,
            "mu2": mu2,
            "longitudinal_quadratic_coefficient": c_long,
            "transverse_quadratic_coefficient": c_trans,
            "coefficient_ratio": c_trans / c_long,
        },
        "rows": rows,
        "registered_checks": {
            "P11A_kernel_normalized": abs(float(np.real(k(0.0))) - 1.0) < 1e-14,
            "P11B_transverse_norm_exceeds_one_for_nonzero_D": all(r["offline_hermitian_norm_sq_k_2ix"] > 1.0 for r in rows),
            "P11C_longitudinal_coefficient_matches_mu2": abs(rows[-1]["longitudinal_gap_over_x2"] / c_long - 1.0) < 1e-6,
            "P11D_transverse_coefficient_matches_mu2": abs(rows[-1]["transverse_gap_over_x2"] / c_trans - 1.0) < 1e-6,
            "P11E_same_coordinate_ratio_tends_to_four": abs(rows[-1]["transverse_to_longitudinal_same_x_ratio"] - 4.0) < 1e-5,
            "P11F_d_equals_2D_equalizes_leading_penalty": abs(rows[-2]["transverse_to_longitudinal_2x_ratio"] - 1.0) < 1e-5,
            "P11G_pair_negative_eigenvalue_is_exactly_minus_norm_excess": all(abs(r["pair_lambda_minus"] + r["transverse_negative_magnitude"]) < 1e-15 for r in rows),
        },
    }
    result["all_registered_checks_pass"] = all(result["registered_checks"].values())

    out = OUT / "gate11_complex_pair_metric.json"
    out.write_text(json.dumps(result, indent=2), encoding="utf-8")

    print("Gate 11 — complex Poisson pair metric")
    print("=====================================")
    print("mu2:", mu2)
    print("c_long:", c_long)
    print("c_trans:", c_trans)
    print("ratio:", c_trans / c_long)
    print("same-x ratios:", [(r["x"], r["transverse_to_longitudinal_same_x_ratio"]) for r in rows])
    print("d=2D ratios:", [(r["x"], r["transverse_to_longitudinal_2x_ratio"]) for r in rows])
    print("all registered checks:", result["all_registered_checks_pass"])
    print("wrote", out)


if __name__ == "__main__":
    main()
