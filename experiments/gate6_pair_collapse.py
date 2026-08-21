#!/usr/bin/env python3
"""
Gate 6 — safe smoothed-L2 certificate collapses to pair information.

No RH claim. The experiment checks the configuration-wise multiplicity bound

    simple_fraction >= 2 - Q / (N R(0)),

where R(u)=|K_B(u)|^2 >= 0 and K_B is the Gate-5 bandlimited Poisson atom.

For marks in {1,2}, sum m_i^2 = 2N-S exactly, so separated points make the
bound approach equality as off-diagonal R terms decay.

Dependency: numpy.
"""

import json
import math
from pathlib import Path

import numpy as np

OUT = Path("results")
OUT.mkdir(exist_ok=True)
PI = math.pi

ETA = 0.5
ATOM_BANDWIDTH = 0.4
PAIR_BANDWIDTH = 2.0 * ATOM_BANDWIDTH


def K_real(u: float, eta: float = ETA, bandwidth: float = ATOM_BANDWIDTH, n: int = 16001) -> float:
    xi = np.linspace(0.0, bandwidth, n)
    hat = -4.0 * PI**2 * xi * np.exp(-2.0 * PI * eta * xi)
    return float(2.0 * np.trapezoid(hat * np.cos(2.0 * PI * xi * u), xi))


def R_nonnegative(u: float) -> float:
    k = K_real(u)
    return k * k


def certificate(points, multiplicities):
    points = np.asarray(points, dtype=float)
    multiplicities = np.asarray(multiplicities, dtype=int)
    N = int(np.sum(multiplicities))
    S = int(np.sum(multiplicities == 1))

    diffs = points[:, None] - points[None, :]
    kernel = {float(d): R_nonnegative(float(d)) for d in np.unique(diffs)}

    Q = 0.0
    for i in range(len(points)):
        for j in range(len(points)):
            Q += multiplicities[i] * multiplicities[j] * kernel[float(diffs[i, j])]

    R0 = R_nonnegative(0.0)
    lower = 2.0 - Q / (N * R0)
    actual = S / N
    m2 = int(np.sum(multiplicities**2))

    return {
        "N_total_multiplicity": N,
        "S_simple_points": S,
        "actual_simple_fraction": actual,
        "sum_m_squared": m2,
        "twoN_minus_S": 2 * N - S,
        "multiplicity_inequality_slack": m2 - (2 * N - S),
        "Q": Q,
        "R0": R0,
        "certificate_lower_bound": lower,
        "bound_holds": lower <= actual + 1e-10,
    }


def main():
    marks = np.array([1, 1, 1, 2, 2, 2], dtype=int)
    spacing_rows = []
    for spacing in [2.0, 5.0, 10.0, 20.0, 50.0]:
        points = np.arange(len(marks), dtype=float) * spacing
        row = certificate(points, marks)
        row["spacing"] = spacing
        spacing_rows.append(row)

    rng = np.random.default_rng(20260821)
    random_rows = []
    for _ in range(8):
        points = np.sort(rng.uniform(0.0, 30.0, 8))
        random_marks = rng.integers(1, 3, size=8)  # marks 1 or 2
        row = certificate(points, random_marks)
        row["points"] = points.tolist()
        row["marks"] = random_marks.tolist()
        random_rows.append(row)

    result = {
        "gate": "gate6-pair-collapse",
        "status": "safe_L2_certificate_is_pair_form_factor_class",
        "atom_eta": ETA,
        "atom_fourier_support": [-ATOM_BANDWIDTH, ATOM_BANDWIDTH],
        "pair_fourier_support": [-PAIR_BANDWIDTH, PAIR_BANDWIDTH],
        "inside_bandwidth_one": PAIR_BANDWIDTH < 1.0,
        "certificate": "S/N >= 2 - Q/(N*R0), R=|K_B|^2",
        "separated_marked_configuration": spacing_rows,
        "random_marked_configurations": random_rows,
        "registered_checks": {
            "P6A_pair_bandwidth_below_one": PAIR_BANDWIDTH < 1.0,
            "P6B_all_configuration_bounds_hold": all(r["bound_holds"] for r in spacing_rows + random_rows),
            "P6C_marks_1_2_make_multiplicity_step_exact": all(r["multiplicity_inequality_slack"] == 0 for r in spacing_rows + random_rows),
            "P6D_separated_example_approaches_actual_fraction": abs(spacing_rows[-1]["certificate_lower_bound"] - spacing_rows[-1]["actual_simple_fraction"]) < 1e-5,
        },
    }
    result["all_registered_checks_pass"] = all(result["registered_checks"].values())

    out = OUT / "gate6_pair_collapse.json"
    out.write_text(json.dumps(result, indent=2), encoding="utf-8")

    print("Gate 6 — pair collapse")
    print("======================")
    print("pair support:", result["pair_fourier_support"])
    print("spacing bounds:", [(r["spacing"], r["certificate_lower_bound"]) for r in spacing_rows])
    print("all registered checks:", result["all_registered_checks_pass"])
    print("wrote", out)


if __name__ == "__main__":
    main()
