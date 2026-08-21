#!/usr/bin/env python3
"""
Gate 7 — finite derivative channels versus the homometric attacker.

No RH claim. We construct a matrix-valued translation-invariant Gram kernel
from compactly supported Fourier-side derivative channels

    q_r(xi) = (2*pi*i*xi)^r sqrt(w(xi)), r=0..R,

then compare the homometric configurations
A={0,1,4,10,12,17}, B={0,1,8,11,13,17}.

Registered prediction:
- trace and Frobenius norm squared tie for every finite channel order;
- tr(G^3) is allowed to separate because it is a closed-triangle statistic.

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
B = np.array([0, 1, 8, 11, 13, 17], dtype=float)
BANDWIDTH = 0.4


def block_gram(points, order, nfreq=8001):
    xi = np.linspace(-BANDWIDTH, BANDWIDTH, nfreq)
    # Smooth nonnegative taper, zero at the support endpoints.
    w = np.cos(PI * xi / (2.0 * BANDWIDTH)) ** 2
    sqrtw = np.sqrt(w)
    channels = [(2j * PI * xi) ** r * sqrtw for r in range(order + 1)]

    c = order + 1
    n = len(points)
    G = np.empty((n * c, n * c), dtype=complex)

    diffs = np.unique((points[:, None] - points[None, :]).ravel())
    cache = {}
    for d in diffs:
        phase = np.exp(2j * PI * xi * d)
        K = np.empty((c, c), dtype=complex)
        for r in range(c):
            for s in range(c):
                K[r, s] = np.trapezoid(
                    channels[r] * np.conj(channels[s]) * phase,
                    xi,
                )
        cache[float(d)] = K

    for i in range(n):
        for j in range(n):
            G[i*c:(i+1)*c, j*c:(j+1)*c] = cache[float(points[i] - points[j])]

    return G


def measurements(G):
    return {
        "trace": float(np.trace(G).real),
        "frobenius_squared": float(np.linalg.norm(G, "fro") ** 2),
        "trace_cube": float(np.trace(G @ G @ G).real),
        "hermitian_error": float(np.linalg.norm(G - G.conj().T, "fro")),
    }


def main():
    rows = []
    for order in [0, 1, 2, 3]:
        GA = block_gram(A, order)
        GB = block_gram(B, order)
        a = measurements(GA)
        b = measurements(GB)
        rows.append({
            "max_derivative_order": order,
            "channels": order + 1,
            "A": a,
            "B": b,
            "absolute_differences": {
                "trace": abs(a["trace"] - b["trace"]),
                "frobenius_squared": abs(a["frobenius_squared"] - b["frobenius_squared"]),
                "trace_cube": abs(a["trace_cube"] - b["trace_cube"]),
            },
        })

    result = {
        "gate": "gate7-jet-channels",
        "status": "finite_derivative_channels_do_not_escape_two_moment_pair_data",
        "bandwidth": BANDWIDTH,
        "set_A": A.astype(int).tolist(),
        "set_B": B.astype(int).tolist(),
        "rows": rows,
        "registered_checks": {
            "P7A_trace_ties_all_orders": all(r["absolute_differences"]["trace"] < 1e-10 for r in rows),
            "P7B_frobenius_ties_all_orders": all(r["absolute_differences"]["frobenius_squared"] < 1e-10 for r in rows),
            "P7C_some_third_moment_separates": any(r["absolute_differences"]["trace_cube"] > 1e-5 for r in rows),
            "P7D_all_matrices_hermitian": all(max(r["A"]["hermitian_error"], r["B"]["hermitian_error"]) < 1e-10 for r in rows),
        },
    }
    result["all_registered_checks_pass"] = all(result["registered_checks"].values())

    out = OUT / "gate7_jet_channels.json"
    out.write_text(json.dumps(result, indent=2), encoding="utf-8")

    print("Gate 7 — derivative jet channels")
    print("================================")
    for r in rows:
        print(r["max_derivative_order"], r["absolute_differences"])
    print("all registered checks:", result["all_registered_checks_pass"])
    print("wrote", out)


if __name__ == "__main__":
    main()
