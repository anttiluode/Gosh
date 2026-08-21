# Gate 1 — Contracting Bandwidth

## Question

Gate 0 killed the literal idea that AnttisBrain2's `four bounces = observational infinity` could be transplanted to the critical-line Dirichlet series. The useful residue was different:

> the truncation depth is set by the resolution of the **observer / certificate**, not by a universal magic number.

Claude's 2026 rank–trace argument gives us an unusually concrete observer: a finite Hermitian compression whose low trace moments constrain **inertia**, and therefore how much off-line zero structure can be present.

The same paper also points to the next obstruction. Higher trace moments would carry more information, but at full arithmetic bandwidth they demand higher prime correlations beyond the presently unconditional input. This suggested the deliberately modest question:

> **If moment order increases while arithmetic bandwidth decreases, can coarse higher-order information contain configuration information that all pair-level measurements miss?**

This gate asks only the information question. It does **not** claim that such a moment can yet be supplied unconditionally on the prime side, nor that several different compressions can yet be combined into a valid zeta-zero certificate.

---

## Prior-art correction before the experiment

The phrase `higher order -> narrower bandwidth` is not new mathematics.

Restricted Fourier support is already fundamental in rigorous n-level correlation results for zeta and principal L-functions, notably Rudnick–Sarnak. Very roughly, increasing correlation order forces a restriction on the total Fourier support if one wants unconditional control. Claude's paper is operating inside this same arithmetic geometry when it discusses what higher Gram moments would require.

So Gate 1 does **not** claim a new support principle. The only potentially useful question left is architectural:

> can several resolutions be used **jointly** — sharp pair information at large bandwidth and blurrier higher-order information at smaller bandwidth — in one configuration-wise inertia argument?

That question is not answered here.

---

## Why a homometric pair is the right attacker

A weak toy would compare two generic point clouds and announce that `tr(G^4)` differs. Of course it would.

Instead use the non-congruent homometric pair

\[
A=\{0,1,4,10,12,17\},
\qquad
B=\{0,1,8,11,13,17\}.
\]

These two sets have exactly the same multiset of pairwise distances, yet one is not a translation or reflection of the other.

That makes them an adversarial pair for **all pair-level measurements** built from a translation-invariant kernel.

Let

\[
G_\theta(x)_{ij}=K_\theta(x_i-x_j)
\]

with an even translation-invariant kernel. In the experiment

\[
K_\theta(d)=\operatorname{sinc}(\theta d).
\]

Then

\[
\operatorname{tr}G_\theta^2
=\sum_{ij}|K_\theta(x_i-x_j)|^2
\]

depends only on the multiset of pairwise differences/distances. Therefore the homometric pair ties in `tr(G^2)` **for every bandwidth**, not merely for a hand-picked value of `theta`.

`tr(G)` also ties trivially because the diagonal is the same.

This is exactly the kind of control we wanted: if a higher moment separates the pair, it has found information that no translation-invariant pair statistic can recover.

---

## Why higher traces can escape pair data

For `k >= 3`,

\[
\operatorname{tr}G^k
=\sum_{i_1,\ldots,i_k}
K(x_{i_1}-x_{i_2})
K(x_{i_2}-x_{i_3})\cdots
K(x_{i_k}-x_{i_1}).
\]

This is a weighted sum over closed walks.

A pair-distance multiset tells us **which edge lengths exist and how often**. It does not tell us how those edges are assembled into triangles, quadrilaterals, and longer closed walks. Homometric sets can therefore have identical pair information and different higher closed-walk information.

This is the clean mathematical bridge back to the old `HilbertPolyaReintepretation` / prime-loop language: the useful object there was not the speculative physical story but the fact that traces of powers enumerate closed walks.

---

## Registered predictions

Before the run:

1. **P1:** `A` and `B` are homometric but not congruent under translation/reflection.
2. **P2:** `tr(G)` and `tr(G^2)` tie to numerical precision at every tested bandwidth.
3. **P3:** at some deliberately contracted bandwidth satisfying the toy budget

   \[
   4\theta<2,
   \]

   the fourth trace differs.

The last inequality is only a mnemonic analogue of the restricted-support arithmetic budget discussed in the higher-moment literature. It is **not** a theorem transferring the toy to zeta.

---

## Result

All three registered predictions passed.

| theta | pair-level `|Δ tr G²|` | `|Δ tr G³|` | `|Δ tr G⁴|` | toy `4 theta < 2` |
|---:|---:|---:|---:|:---:|
| 0.8 | 1.8e-15 | 0.00950 | 0.03647 | no |
| 0.6 | 1.8e-15 | 0.05658 | 0.19884 | no |
| 0.5 | 2.7e-15 | ~0 | 0.06565 | no |
| **0.4** | **1.8e-15** | **0.19095** | **0.90291** | **yes** |
| 0.3 | 1.8e-15 | 0.18530 | 0.73916 | yes |
| 0.2 | 5.3e-15 | 0.60812 | 2.82629 | yes |

At `theta=0.4`, pair information is tied to machine precision while the fourth closed-walk moment differs by about `0.903`.

The result is stronger than `a higher moment contains more information` in the generic sense:

> **coarse higher-order information distinguishes two configurations that every translation-invariant pair-distance statistic, at every bandwidth, necessarily identifies.**

That is a real information-theoretic fact about the toy.

---

## What this does NOT establish

This is where the Riemann wall remains intact.

### 1. It does not provide the arithmetic moment

The toy computes the matrix directly from a known point configuration. In the zeta problem, the whole challenge is to obtain the needed matrix statistic from the **prime side without assuming the zero configuration**. Restricted-support theorems tell us which higher correlations are arithmetically accessible; this script proves none of those estimates.

### 2. It does not combine different bandwidths into one theorem

A full-bandwidth Gram matrix and a narrower-bandwidth Gram matrix are different Hermitian objects. One cannot simply put their traces in the same inequality and pretend they describe one matrix.

A valid continuation must identify a common latent object — the same zero configuration / multiplicity blocks — and prove a joint inequality that both compressions constrain.

### 3. It does not beat the bandwidth-one ceiling

Claude's bandwidth-one ceiling concerns a particular class of certificates built from pair/form-factor information. The homometric example merely demonstrates why leaving the pair-information class can matter. It gives no new numerical lower bound for zeta zeros.

### 4. `theta` is not literally the paper's support parameter

The sinc toy was chosen because it makes the information distinction transparent. The line `4 theta < 2` is a design analogy, not an identification with a particular Weil test function normalization.

---

## Gate 1 verdict

**Positive reconnaissance, not mathematical progress on RH.**

The naive Gate 1 claim

> `narrower bandwidth makes higher moments new`

would be mostly prior art and is rejected.

The surviving statement is narrower:

> **pair-level information can remain exactly degenerate across every resolution while a lower-resolution closed-walk moment breaks the degeneracy. Therefore a multiresolution certificate is not information-theoretically redundant by construction.**

That justifies one more gate.

---

# Gate 2 candidate — the joint-certificate problem

The next problem should not compute more pretty moments. It should ask whether the information can legally meet.

Let a common zero configuration `Z` generate two Hermitian compressions

\[
G_{\rm sharp}(Z),\qquad G_{\rm coarse}(Z),
\]

where the sharp compression has unconditional pair-level arithmetic data and the coarse compression is chosen so that some higher moment lies inside a rigorous restricted-support range.

The desired object is an inequality of the form

\[
\mathcal C\big(
\operatorname{tr}G_{\rm sharp},
\operatorname{tr}G_{\rm sharp}^2,
\operatorname{tr}G_{\rm coarse}^2,
\operatorname{tr}G_{\rm coarse}^4,
\ldots
\big)
\le / \ge
F(\text{number or multiplicity of on-line atoms}),
\]

valid **for every admissible zero configuration**, not merely for a random-matrix model.

If no such inequality can improve the known pair certificate even on finite synthetic block models, stop. If one exists numerically, derive it as a finite-dimensional extremal problem before touching zeta arithmetic.

### Gate 2 stop lines

- same latent zero/block configuration feeds every aperture;
- off-line conjugate/reflected blocks must be represented explicitly;
- no random-matrix average may replace a worst-case inequality;
- all arithmetic inputs must be labelled unconditional / conditional separately;
- if the only useful coarse fourth moment requires the same Hardy–Littlewood input Claude already identifies, record the wall and stop.

---

## Files

```text
experiments/gate1_contracting_bandwidth.py
results/gate1_contracting_bandwidth.json
```

Run:

```bash
pip install numpy
python experiments/gate1_contracting_bandwidth.py
```

---

## References / context

- Claude, *More than two thirds of the zeros of the Riemann zeta function are simple and on the critical line* (2026), especially the rank–trace mechanism, bandwidth-one ceiling, and discussion of higher moments.
- Z. Rudnick and P. Sarnak, *Zeros of principal L-functions and random matrix theory*, Duke Math. J. 81 (1996), for rigorous higher correlation under restricted Fourier support.
- `AnttisBrain2/resolution_horizon.md` and `HorizonNet` for the observation-horizon lineage.
- `HilbertPolyaReintepretation` and `Alkuluku` for the closed-walk / prime-trace and falsification lineage.

---

*The point of Gate 1 is not that blur magically creates information. It is that order and resolution are different axes: a blurry triangle can contain something a perfectly sharp bag of edges does not.*
