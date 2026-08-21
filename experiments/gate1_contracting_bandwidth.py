#!/usr/bin/env python3
"""
Gate 1 reconnaissance — Contracting bandwidth can preserve higher-order information

This is an information toy, NOT a zeta computation.

We use a classical non-congruent homometric pair of point sets:
    A = {0,1,4,10,12,17}
    B = {0,1,8,11,13,17}

They have the same multiset of pairwise distances. Therefore for every
translation-invariant even kernel k_theta(x-y), any statistic depending only on
pair data (including tr(G) and tr(G^2) for the Gram matrix
G_ij = k_theta(x_i-x_j)) is identical for A and B at EVERY bandwidth theta.

Higher traces depend on closed triangles / longer walks and can distinguish
how those same pairwise distances are assembled.

The AnttisBrain-shaped question:
Can a higher moment at LOWER bandwidth carry genuinely new configuration
information, even when all pair-level observations at every bandwidth tie?

Registered predictions:
P1: A and B are homometric but not related by translation/reflection.
P2: tr(G_theta) and tr(G_theta^2) agree to numerical precision for every tested theta.
P3: at some theta with 4*theta < 2 (a toy analogue of X^k < T^2),
    tr(G_theta^4) differs between A and B.
"""

import json
from collections import Counter
from pathlib import Path

import numpy as np


OUT = Path("results")
OUT.mkdir(exist_ok=True)

A = np.array([0, 1, 4, 10, 12, 17], dtype=float)
B = np.array([0, 1, 8, 11, 13, 17], dtype=float)


def distance_multiset(x):
    vals = []
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            vals.append(float(abs(x[j] - x[i])))
    return Counter(vals)


def congruent_1d(a, b):
    """Check equality up to translation and reflection."""
    a = np.sort(np.asarray(a, dtype=float))
    b = np.sort(np.asarray(b, dtype=float))
    a0 = a - a[0]
    b0 = b - b[0]
    if np.allclose(a0, b0):
        return True
    reflected = np.sort(a[-1] - a)
    reflected -= reflected[0]
    return np.allclose(reflected, b0)


def sinc_gram(x, theta):
    """
    Translation-invariant overlap toy:
        G_ij = sinc(theta * (x_i-x_j))
    np.sinc(z) = sin(pi z)/(pi z).
    """
    d = x[:, None] - x[None, :]
    return np.sinc(theta * d)


def trace_moments(G, max_order=4):
    eig = np.linalg.eigvalsh(G)
    return {
        str(k): float(np.sum(eig**k))
        for k in range(1, max_order + 1)
    }


def main():
    homometric = distance_multiset(A) == distance_multiset(B)
    noncongruent = not congruent_1d(A, B)

    thetas = [0.8, 0.6, 0.5, 0.4, 0.3, 0.2]
    rows = []
    pair_tie_all = True
    coarse_higher_separates = False

    for theta in thetas:
        GA = sinc_gram(A, theta)
        GB = sinc_gram(B, theta)
        mA = trace_moments(GA)
        mB = trace_moments(GB)

        d1 = abs(mA["1"] - mB["1"])
        d2 = abs(mA["2"] - mB["2"])
        d3 = abs(mA["3"] - mB["3"])
        d4 = abs(mA["4"] - mB["4"])

        pair_tie = d1 < 1e-10 and d2 < 1e-10
        pair_tie_all &= pair_tie

        # Deliberately strict version of the schematic arithmetic budget k*theta < 2.
        legal4_toy_budget = 4.0 * theta < 2.0
        if legal4_toy_budget and d4 > 1e-4:
            coarse_higher_separates = True

        rows.append({
            "theta": theta,
            "toy_budget_4theta_lt_2": legal4_toy_budget,
            "trace_moments_A": mA,
            "trace_moments_B": mB,
            "abs_diff_tr1": d1,
            "abs_diff_tr2": d2,
            "abs_diff_tr3": d3,
            "abs_diff_tr4": d4,
            "pair_level_tie": pair_tie,
        })

    result = {
        "gate": "gate1-contracting-bandwidth-recon",
        "status": "information_toy_not_a_zeta_certificate",
        "set_A": A.astype(int).tolist(),
        "set_B": B.astype(int).tolist(),
        "homometric_same_pairwise_distance_multiset": homometric,
        "noncongruent_under_translation_or_reflection": noncongruent,
        "rows": rows,
        "P1_homometric_noncongruent": homometric and noncongruent,
        "P2_pair_data_tie_every_tested_bandwidth": pair_tie_all,
        "P3_coarse_fourth_moment_separates_under_toy_budget": coarse_higher_separates,
    }
    result["all_registered_predictions_pass"] = all(
        [result["P1_homometric_noncongruent"],
         result["P2_pair_data_tie_every_tested_bandwidth"],
         result["P3_coarse_fourth_moment_separates_under_toy_budget"]]
    )

    out = OUT / "gate1_contracting_bandwidth.json"
    out.write_text(json.dumps(result, indent=2), encoding="utf-8")

    print("Gate 1 — contracting bandwidth reconnaissance")
    print("============================================")
    print("homometric:", homometric, "noncongruent:", noncongruent)
    for r in rows:
        print(
            f"theta={r['theta']:.1f}  "
            f"|Δtr2|={r['abs_diff_tr2']:.3e}  "
            f"|Δtr3|={r['abs_diff_tr3']:.6f}  "
            f"|Δtr4|={r['abs_diff_tr4']:.6f}  "
            f"4theta<2={r['toy_budget_4theta_lt_2']}"
        )
    print("all registered predictions:", result["all_registered_predictions_pass"])
    print("wrote", out)


if __name__ == "__main__":
    main()
