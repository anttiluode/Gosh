#!/usr/bin/env python3
"""
Gate 3 — Clockfield valley -> Laguerre hierarchy -> resolution horizon

This is a falsification / structure experiment, not an RH proof attempt.

The ClockfieldRiemann "valley" quantity is the first generalized Laguerre
coefficient of Xi(t)=xi(1/2+it).  Fable's July 2026 audit correctly notes that
L1 >= 0 is necessary under RH but is not by itself equivalent to RH; the full
Laguerre hierarchy is the classical real-zero criterion.

This gate checks four things:

P3A  Fable's strip-interior counterexample passes the first valley test but is
     caught by the second Laguerre coefficient.
P3B  In the analytic fake family cos(k z)(z^2+a^2), local detection depth grows
     with the dimensionless product a*k; there is no universal fixed "four".
P3C  The bandlimited Poisson-curvature attenuation and the actual L2 signature
     distance both collapse to functions of x=a*B (off-line displacement times
     observer bandwidth), but have different small-x laws: linear attenuation,
     quadratic metric distance.
P3D  Claude's Gate-2b conjecture that pushing the mixed-aperture allocation all
     the way toward two huge / two blind legs should keep improving is false.

Dependencies: numpy only.
"""

import json
import math
from pathlib import Path

import numpy as np

OUT = Path("results")
OUT.mkdir(exist_ok=True)
PI = math.pi


# ---------------------------------------------------------------------------
# 1. Laguerre hierarchy in Fable's synthetic counterexample
# ---------------------------------------------------------------------------

def fable_fake_L1(x: float, a: float, k: float) -> float:
    """L1=f'^2-f f'' for f(x)=cos(kx)(x^2+a^2)."""
    c = math.cos(k * x)
    s = math.sin(k * x)
    f = c * (x * x + a * a)
    fp = -k * s * (x * x + a * a) + 2.0 * x * c
    fpp = -k * k * c * (x * x + a * a) - 4.0 * k * x * s + 2.0 * c
    return fp * fp - f * fpp


def laguerre_L1_L2_at_zero(a: float, k: float):
    """
    At x=0,
      |f(iy)|^2 = cosh^2(k y) (a^2-y^2)^2
                = L0 + L1 y^2 + L2 y^4 + ...
    with q=(ak)^2.
    """
    q = (a * k) ** 2
    L1 = a * a * (q - 2.0)
    L2 = q * q / 3.0 - 2.0 * q + 1.0
    return q, L1, L2


def normalized_Ln_sign(n: int, q: float) -> float:
    """
    Sign-equivalent normalized coefficient L_n(0) for n>=1, q=(ak)^2.

    For n>=3, using cosh^2(k y) coefficients gives
      sign L_n = sign[1 - 8q/B + 16q^2/(A B)]
      A=(2n)(2n-1), B=(2n-2)(2n-3).
    """
    if n == 1:
        return q - 2.0
    if n == 2:
        return q * q / 3.0 - 2.0 * q + 1.0
    A = (2 * n) * (2 * n - 1)
    B = (2 * n - 2) * (2 * n - 3)
    return 1.0 - 8.0 * q / B + 16.0 * q * q / (A * B)


def first_negative_order(q: float, max_order: int = 1000):
    for n in range(1, max_order + 1):
        value = normalized_Ln_sign(n, q)
        if value < 0.0:
            return n, value
    return None, None


# ---------------------------------------------------------------------------
# 2. Bandlimited Poisson-curvature observables
# ---------------------------------------------------------------------------

def int_u2_exp(c: float) -> float:
    """Integral_0^1 u^2 exp(-c u) du, stable near c=0."""
    if abs(c) < 0.5:
        # Sum (-c)^m / (m! (m+3)).
        term = 1.0
        total = 0.0
        for m in range(200):
            if m:
                term *= -c / m
            add = term / (m + 3)
            total += add
            if abs(add) < 1e-18:
                break
        return total
    return (2.0 - math.exp(-c) * (c * c + 2.0 * c + 2.0)) / (c ** 3)


def energy_attenuation_ratio(x: float) -> float:
    """
    1 - E_B(a)/E_B(0), where x=aB and
      E_B(a) proportional to integral_0^B xi^2 exp(-4 pi a xi) dxi.

    This is attenuation of signature energy, not a metric distance.
    """
    c = 4.0 * PI * x
    return 1.0 - 3.0 * int_u2_exp(c)


def l2_signature_distance_ratio(x: float) -> float:
    """
    ||C_0-C_a||^2 over |xi|<=B, normalized by ||C_0||^2.
    After xi=B u this depends only on x=aB:
      3 integral_0^1 u^2 (1-exp(-2 pi x u))^2 du.
    """
    c = 2.0 * PI * x
    return 1.0 - 6.0 * int_u2_exp(c) + 3.0 * int_u2_exp(2.0 * c)


# ---------------------------------------------------------------------------
# 3. Gate-2b attacker: extreme aperture allocation
# ---------------------------------------------------------------------------
A_SET = np.array([0, 1, 4, 10, 12, 17], dtype=float)
B_SET = np.array([0, 1, 8, 11, 13, 17], dtype=float)


def gram(points, theta):
    d = points[:, None] - points[None, :]
    return np.sinc(theta * d)


def mixed_trace(points, thetas):
    M = np.eye(len(points))
    for theta in thetas:
        M = M @ gram(points, theta)
    return float(np.trace(M))


def separation(thetas):
    return abs(mixed_trace(A_SET, thetas) - mixed_trace(B_SET, thetas))


def main():
    # Fable's strip-interior fake: cos(pi t/0.8)*(t^2+0.16).
    a = 0.4
    k = PI / 0.8
    q, L1_0, L2_0 = laguerre_L1_L2_at_zero(a, k)

    xs = np.linspace(0.0, 40.0, 40001)
    L1_vals = np.array([fable_fake_L1(float(x), a, k) for x in xs])
    idx = int(np.argmin(L1_vals))
    fable_scan = {
        "a": a,
        "k": k,
        "ak": a * k,
        "q_ak_squared": q,
        "scan_interval": [0.0, 40.0],
        "scan_step": 0.001,
        "min_L1": float(L1_vals[idx]),
        "argmin_L1": float(xs[idx]),
        "L1_at_zero": L1_0,
        "L2_at_zero": L2_0,
        "L1_passes_scan": bool(np.min(L1_vals) > 0.0),
        "L2_catches_at_zero": bool(L2_0 < 0.0),
    }

    q_values = [q, 6.0, 10.0, 20.0, 50.0, 100.0, 200.0, 500.0, 1000.0]
    depth_rows = []
    for qv in q_values:
        n, val = first_negative_order(qv)
        depth_rows.append({
            "q": qv,
            "ak": math.sqrt(qv),
            "first_negative_order_at_x0": n,
            "normalized_value": val,
            "order_over_ak": (n / math.sqrt(qv)) if n is not None else None,
        })

    x_values = [1e-4, 1e-3, 1e-2, 5e-2, 1e-1]
    bandwidth_rows = []
    linear_coeff = 3.0 * PI
    quadratic_coeff = 12.0 * PI * PI / 5.0
    for x in x_values:
        att = energy_attenuation_ratio(x)
        dist = l2_signature_distance_ratio(x)
        bandwidth_rows.append({
            "x_a_times_B": x,
            "energy_attenuation": att,
            "attenuation_over_3pi_x": att / (linear_coeff * x),
            "l2_signature_distance": dist,
            "distance_over_12pi2_over5_x2": dist / (quadratic_coeff * x * x),
        })

    allocations = [
        (0.4, 0.4, 0.4, 0.4),
        (0.70, 0.05, 0.70, 0.15),
        (0.78, 0.02, 0.78, 0.02),
        (0.79, 0.01, 0.79, 0.01),
        (0.80, 0.00, 0.80, 0.00),
    ]
    gate2b_rows = [
        {"thetas": list(t), "abs_separation": separation(t)} for t in allocations
    ]

    known_best = gate2b_rows[1]["abs_separation"]
    extreme = gate2b_rows[2]["abs_separation"]
    blind_limit = gate2b_rows[-1]["abs_separation"]

    result = {
        "gate": "gate3-laguerre-horizon",
        "status": "structure_and_falsification_toy_not_RH_progress",
        "clockfield_fable_attacker": fable_scan,
        "laguerre_detection_depth_at_symmetry_point": depth_rows,
        "poisson_bandlimit": {
            "note": "energy attenuation is not the same as metric discrimination",
            "small_x_energy_attenuation": "3*pi*x + O(x^2)",
            "small_x_l2_signature_distance": "(12*pi^2/5)*x^2 + O(x^3)",
            "rows": bandwidth_rows,
        },
        "gate2b_extreme_allocation_attack": gate2b_rows,
        "registered_checks": {
            "P3A_L1_passes_but_L2_catches_fable_fake": bool(fable_scan["L1_passes_scan"] and fable_scan["L2_catches_at_zero"]),
            "P3B_detection_depth_not_fixed": bool(depth_rows[-1]["first_negative_order_at_x0"] > depth_rows[0]["first_negative_order_at_x0"]),
            "P3C_small_x_scalings_match": bool(
                abs(bandwidth_rows[0]["attenuation_over_3pi_x"] - 1.0) < 1e-3
                and abs(bandwidth_rows[0]["distance_over_12pi2_over5_x2"] - 1.0) < 1e-3
            ),
            "P3D_extreme_edge_loading_prediction_fails": bool(extreme < known_best and blind_limit < 1e-10),
        },
    }
    result["all_registered_checks_pass"] = all(result["registered_checks"].values())

    out = OUT / "gate3_laguerre_horizon.json"
    out.write_text(json.dumps(result, indent=2), encoding="utf-8")

    print("Gate 3 — Laguerre resolution horizon")
    print("====================================")
    print("Fable fake: min L1 on [0,40] =", fable_scan["min_L1"])
    print("Fable fake: L2(0) =", fable_scan["L2_at_zero"])
    print("first-negative orders:", [(r["ak"], r["first_negative_order_at_x0"]) for r in depth_rows])
    print("Gate2b known best / extreme / blind limit =", known_best, extreme, blind_limit)
    print("all registered checks:", result["all_registered_checks_pass"])
    print("wrote", out)


if __name__ == "__main__":
    main()
