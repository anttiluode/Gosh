# Gate 2 — Mixed-Aperture Closed Walks

## Why Gate 2 exists

Gate 1 used a homometric pair to show that pair information can be **exactly identical at every bandwidth** while higher closed-walk moments differ. That was enough to show that higher-order information is not redundant with pair data.

But simply computing `tr(G_theta^4)` at a smaller `theta` still treats every leg of the closed walk at the same resolution.

AnttisBrain2 did something more structural than `make everything blurry`: every additional bounce was another application of the same process, and the useful resolution was whatever survived along the path.

The natural matrix analogue is therefore a **mixed-aperture closed walk**:

\[
T(\theta_1,\ldots,\theta_k)
=
\operatorname{tr}
\left(
G_{\theta_1}G_{\theta_2}\cdots G_{\theta_k}
\right).
\]

Every leg sees the same latent configuration, but not necessarily at the same resolution.

This gate asks only:

> **Under a fixed total toy resolution budget, does unequal resolution allocation carry more configuration information than equal allocation?**

Again: this is an information toy, not an arithmetic support theorem.

---

## Prior art before the result

Unequal test functions / unequal Fourier supports are not a new concept.

Restricted-support n-level density already allows nontrivial support geometry, and recent work on families of automorphic L-functions has explicitly found cases where choosing **different test functions with different supports** extends the range in which density predictions can be proved. Cheek, Gilman, Jaber, Miller, and Tomé describe this as the mechanism behind an extension of their two-level support range.

That work concerns a different L-function-family setting and makes assumptions not available here, so it does not answer the `Gosh` question. But it kills any novelty claim of the form

> `we invented unequal support allocation.`

We did not.

The only possible point here is narrower: whether mixed-resolution traces can be made useful **inside the specific Hermitian inertia architecture of Claude's zeta argument**.

---

## The same homometric attacker

Keep

\[
A=\{0,1,4,10,12,17\},
\qquad
B=\{0,1,8,11,13,17\}.
\]

and

\[
G_\theta(x)_{ij}=\operatorname{sinc}(\theta(x_i-x_j)).
\]

Because the pair is homometric, every two-leg mixed trace

\[
\operatorname{tr}(G_aG_b)
=
\sum_{ij} K_a(x_i-x_j)K_b(x_j-x_i)
\]

depends only on pairwise distances and must tie for `A` and `B`, even when `a != b`.

This gives Gate 2 a strong negative control: merely giving the two legs different resolutions must **not** manufacture a distinction.

Representative checks:

```text
(a,b)       |Δ tr(G_a G_b)|
(.8,.8)      8.9e-16
(1.0,.6)     0
(.7,.1)      0
(.4,.4)      0
(.95,.05)    8.9e-16
```

The control holds.

---

## Fixed total toy budget

For the fourth-order walk, impose

\[
\theta_1+\theta_2+\theta_3+\theta_4=1.6,
\]

with

\[
0.05\le\theta_i\le1.0.
\]

The number `1.6` is deliberately a **toy support budget**. It is not being equated with the exact Fourier-support region of any zeta theorem.

### Equal allocation

\[
(\theta_1,\theta_2,\theta_3,\theta_4)
=(0.4,0.4,0.4,0.4).
\]

Result:

```text
T_A = 16.2179783812
T_B = 15.3150725250
|ΔT| = 0.9029058562
```

### Exhaustive discrete asymmetric allocation

Sweep all ordered allocations on a `0.05` grid satisfying the same total budget and the per-leg cap.

Best result:

\[
(0.70,0.05,0.70,0.15)
\]

with

```text
T_A = 15.2919990982
T_B = 13.1378269945
|ΔT| = 2.1541721037
```

Improvement over equal allocation:

\[
\frac{2.15417}{0.90291}\approx 2.386.
\]

So the same total toy resolution budget becomes substantially more discriminative when it is distributed unevenly around the closed walk.

**Registered predictions P2A–P2C all passed.**

---

## What the toy is saying

This is not `more bandwidth is better`.

The total is held fixed.

Nor is it `higher moments are better`.

The moment order is held fixed.

What changes is **where the resolution is spent around the loop**.

A useful picture is:

```text
uniform loop:
  medium -> medium -> medium -> medium

best toy loop:
  sharp -> almost blind -> sharp -> coarse
```

The second path can distinguish the homometric configurations much more strongly even though both paths spend the same total aperture.

That is strikingly similar to the older PerceptionLab intuition that computation need not maintain the same resolution everywhere along a trajectory. But mathematically this is simply a mixed product of kernels; no biological or physical interpretation is needed.

---

## Why this is closer to Claude's actual zero-side matrix

The Lean formalization makes the block structure explicit.

For one test-function compression, an on-line zero contributes a positive rank-one term. An off-line reflected pair with evaluation vector

\[
u=x+iy
\]

contributes

\[
m(uu^T+\bar u\bar u^T)
=2m(xx^T-yy^T).
\]

Thus every aperture gives a different evaluation map of the **same latent zero block configuration**, while the on-line/off-line involution and multiplicities remain common.

That is the coupling Gate 2 needs conceptually. A mixed-aperture product does not compare unrelated matrices after the fact; it forms a polynomial from several evaluations of the same underlying blocks.

However, the zeta theorem would need to obtain that mixed polynomial from the arithmetic / prime side. Nothing here does that.

---

# The real next wall: mixed arithmetic moments

The next question is now much sharper than `can the moons help RH?`:

> Given test functions / apertures `phi_1,...,phi_k`, can one evaluate or rigorously bound a mixed quantity corresponding to
>
> \[
> \operatorname{tr}(G_{\phi_1}\cdots G_{\phi_k})
> \]
>
> unconditionally in a support region useful enough to strengthen the inertia certificate?

There are three possible endings.

### Ending A — already known and sufficient

Existing restricted-support n-level correlation machinery may already evaluate precisely this mixed statistic. Then `Gosh` has merely rediscovered the right language, and the real task is to plug the known theorem into the finite-dimensional extremal problem.

### Ending B — known but not sufficient

The mixed statistic may be available only in a support region where the resulting matrix inequality is no stronger than Claude's pair certificate. Then Gate 2 becomes a clean negative.

### Ending C — requires unresolved prime correlations

If the useful asymmetric mixed fourth trace still contains the same Hardy–Littlewood-type prime correlations that block the full fourth moment, then the wall has simply moved notation. Record that and stop.

At this point **C is entirely plausible**.

---

# Gate 3 should be analytic before numerical

Do not search more aperture schedules yet. The toy has done its job.

Gate 3 should take the actual test-function normalization from the 2026 paper and symbolically expand the simplest mixed quantity, starting with

\[
\operatorname{tr}(G_aG_b)
\]

as a sanity check and then a mixed fourth trace such as

\[
\operatorname{tr}(G_aG_bG_cG_d).
\]

For each term, identify:

1. its zero-side block expression;
2. its explicit-formula / prime-side expression;
3. the exact Fourier support condition;
4. whether current unconditional estimates cover it;
5. which prime coincidences / additive correlations appear when they do not.

Only after that should another numerical optimization be run.

---

## Files

```text
experiments/gate2_mixed_aperture_walks.py
results/gate2_mixed_aperture_walks.json
```

Run:

```bash
pip install numpy
python experiments/gate2_mixed_aperture_walks.py
```

---

## Ledger

**Verified toy facts**

- homometry forces every mixed two-leg statistic to tie;
- four-leg mixed traces escape that pair-information class;
- with fixed total toy aperture `1.6`, asymmetric allocation improves the homometric separation by about `2.386x` over equal allocation.

**Known / prior-art neighborhood**

- restricted Fourier support in n-level correlations;
- use of different test functions / asymmetric supports in L-function density problems;
- mixed moments and multilinear spectral statistics generally.

**Not established**

- that `sum theta_i` in this sinc toy equals the relevant arithmetic support budget;
- that the mixed fourth trace is unconditionally available for zeta;
- that it yields a stronger worst-case inertia inequality;
- any improved bound on zeros.

---

*Gate 2 does not say that blur solves arithmetic. It says that under a fixed information budget, where you spend resolution around a closed walk can matter a great deal. The next question belongs to the explicit formula, not to another toy.*
