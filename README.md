# Gosh

An intentionally silly name for a serious falsification workflow around Riemann-adjacent ideas.

> **This repository does not claim a proof of the Riemann Hypothesis.**
>
> Turn an intuition into a small mathematical gate, register what would kill it, and keep the negative result when it dies.

## Why this repo exists

Two unrelated lines collided:

1. **Claude / Alpöge–Furman (August 2026):** a rank–trace / inertia argument proves that more than two thirds of zeta zeros are simple and on the critical line by turning prime-side trace information into constraints on the negative directions of a finite Hermitian compression.
2. **AnttisBrain2 / HorizonNet (July 2026):** an apparently infinite hall of mirror moons needed only four visible bounces because deeper structure fell below the observer's resolution. HorizonNet later supplied the correction: the useful horizon belongs in the **observer / decision**, not automatically in the internal state.

So `Gosh` does **not** ask whether four terms solve an infinite zeta series. They do not. It asks:

> **Can an observation horizon make more arithmetic / spectral information finite-to-certificate without erasing the structure that matters?**

## Branch map

```text
main
│
└── sol/gate0-moon-horizon
      Gate 0A  raw-series contraction                      KILLED
      Gate 0B  Fredholm / Neumann zero-wall               VERIFIED NEGATIVE
      Gate 0C  certificate-space spectral horizon         WORKS IN TOY
      │
      └── sol/gate1-contracting-bandwidth
            homometric pair attacker                      PASSES
            pair data tied at every bandwidth
            coarse higher closed-walk moments separate
            prior-art check: restricted support is known
            │
            └── sol/gate2-mixed-aperture-walks
                  mixed two-leg pair control              TIES AS REQUIRED
                  fixed-budget fourth walk                SEPARATES
                  asymmetric aperture allocation          2.386x TOY GAIN
                  prior-art check: unequal supports known
                  │
                  └── next: explicit-formula mixed-moment audit
```

# Gate 0 — the moons do not truncate zeta

Branch: [`sol/gate0-moon-horizon`](../../tree/sol/gate0-moon-horizon)

Detailed note: [`notes/gate0_moon_horizon.md`](../../blob/sol/gate0-moon-horizon/notes/gate0_moon_horizon.md)

Experiment: [`experiments/gate0_horizon_wall.py`](../../blob/sol/gate0-moon-horizon/experiments/gate0_horizon_wall.py)

Receipt: [`results/gate0_horizon_wall.json`](../../blob/sol/gate0-moon-horizon/results/gate0_horizon_wall.json)

### 0A — raw critical-line series: killed

For `a_n = n^(-1/2-it)`,

```text
|a_(n+1)| / |a_n| = sqrt(n/(n+1)) -> 1.
```

There is no fixed contraction factor below one, and `sum_p p^-1/2` is not absolutely convergent. A universal `four terms = infinity` rule is unavailable. Approximate functional equations / Riemann–Siegel are the legitimate number-theory version of a finite horizon, and their depth grows with height.

### 0B — a contracting determinant hits a zero wall

If

```text
D(s) = det(I - L_s)
```

and `||L_s|| < 1`, Neumann / trace-log tails admit geometric bounds. But `D(s)=0` requires `1` in the spectrum of `L_s`, so the contraction condition fails at the zero itself.

Toy receipt at error `1e-6`:

```text
rho=.8   -> K=69
rho=.9   -> K=152
rho=.99  -> K=1832
rho=.999 -> K=20712
rho=1    -> no geometric certificate
```

A contraction certificate can certify an invertible / zero-free region. It does not breach the zero.

### 0C — the useful transplant is a decision horizon

For Hermitian `G`, if a truncation `G_K` obeys

```text
||G - G_K||_op <= delta_K
```

and

```text
min_j |lambda_j(G_K)| > delta_K,
```

Weyl perturbation says the omitted tail cannot move an eigenvalue through zero. The inertia is already fixed.

```text
AnttisBrain2: omitted image structure < visual resolution
Gosh:         omitted operator tail  < spectral sign margin
```

The deterministic infinite Hermitian toy certifies the long-sum inertia after only `K=2`. **Four disappears; the observation-margin principle survives.** This is standard perturbation theory used as an instrument, not a Riemann result.

# Gate 1 — lower resolution can still carry higher-order structure

Branch: [`sol/gate1-contracting-bandwidth`](../../tree/sol/gate1-contracting-bandwidth)

Detailed note: [`notes/gate1_contracting_bandwidth.md`](../../blob/sol/gate1-contracting-bandwidth/notes/gate1_contracting_bandwidth.md)

Experiment: [`experiments/gate1_contracting_bandwidth.py`](../../blob/sol/gate1-contracting-bandwidth/experiments/gate1_contracting_bandwidth.py)

Receipt: [`results/gate1_contracting_bandwidth.json`](../../blob/sol/gate1-contracting-bandwidth/results/gate1_contracting_bandwidth.json)

The attacker is a non-congruent **homometric pair**:

```text
A = {0,1,4,10,12,17}
B = {0,1,8,11,13,17}
```

They have exactly the same multiset of pairwise distances. Consequently every translation-invariant pair statistic ties, including `tr(G)` and `tr(G^2)` for

```text
G_ij = sinc(theta * (x_i - x_j)).
```

Higher traces escape pair data because they count closed walks rather than a bag of edges.

At `theta=0.4`:

```text
|Δ tr(G^2)|  ≈ 1.8e-15
|Δ tr(G^3)|  ≈ 0.19095
|Δ tr(G^4)|  ≈ 0.90291
```

So coarse higher-order information can contain something that even perfectly sharp pair-distance information cannot contain.

### Prior-art correction

`higher moment -> narrower Fourier support` is **not new**. Restricted-support n-level correlation is established territory, especially Rudnick–Sarnak. Claude's own higher-moment discussion runs into that arithmetic support wall.

The surviving question became whether several resolutions can constrain the **same latent zero configuration** jointly.

# Gate 2 — spend resolution unevenly around the closed walk

Branch: [`sol/gate2-mixed-aperture-walks`](../../tree/sol/gate2-mixed-aperture-walks)

Detailed note: [`notes/gate2_mixed_aperture_walks.md`](../../blob/sol/gate2-mixed-aperture-walks/notes/gate2_mixed_aperture_walks.md)

Experiment: [`experiments/gate2_mixed_aperture_walks.py`](../../blob/sol/gate2-mixed-aperture-walks/experiments/gate2_mixed_aperture_walks.py)

Receipt: [`results/gate2_mixed_aperture_walks.json`](../../blob/sol/gate2-mixed-aperture-walks/results/gate2_mixed_aperture_walks.json)

Instead of one aperture, form a mixed closed walk

```text
tr(G_theta1 G_theta2 G_theta3 G_theta4).
```

All factors still see the same latent configuration.

The homometric pair supplies a strong control: **every mixed two-leg trace ties**, even with unequal apertures, because it still depends only on pairwise distances.

Representative checks:

```text
(theta1,theta2)    |Δ mixed trace|
(.8,.8)             8.9e-16
(1.0,.6)            0
(.7,.1)             0
(.95,.05)           8.9e-16
```

Now fix a fourth-order toy aperture budget

```text
theta1 + theta2 + theta3 + theta4 = 1.6
0.05 <= theta_i <= 1.0.
```

Equal allocation:

```text
(.4,.4,.4,.4) -> separation 0.9029058562
```

Exhaustive `0.05`-grid search, same total budget:

```text
(.70,.05,.70,.15) -> separation 2.1541721037
```

That is a **2.3858x** larger distinction between the same two homometric configurations without increasing the total toy aperture.

The toy says only this:

> **where resolution is spent around a higher-order closed walk can matter as much as how much total resolution is available.**

### Prior-art correction again

Using different test functions / unequal Fourier supports is also not ours. There is existing n-level-density work where asymmetric test-function supports genuinely extend accessible ranges in families of L-functions. `Gosh` keeps this as precedent, not novelty.

What remains specific to this project is the proposed weld to the **rank–trace / inertia** framework.

# Why the zero-side structure makes this at least coherent

The 2026 formalization writes an on-line zero as a positive rank-one contribution. An off-line reflected pair with evaluation vector `u=x+iy` contributes

```text
m(uu^T + conjugate(u) conjugate(u)^T)
    = 2m(xx^T - yy^T).
```

Different test-function apertures therefore produce different evaluation vectors of the **same on-line/off-line block configuration**. That is the common latent object a multi-aperture certificate would have to exploit.

The toy has not supplied the arithmetic side.

# Next target — explicit-formula mixed-moment audit

No more aperture optimization yet.

The next gate should take the actual 2026 normalization and symbolically expand, in order:

```text
tr(G_a G_b)                 # sanity check / pair case
tr(G_a G_b G_c G_d)         # first interesting mixed walk
```

For each term it should identify:

1. the zero-side block expression;
2. the corresponding explicit-formula / prime-side expression;
3. the exact Fourier-support region;
4. whether existing unconditional correlation theorems cover it;
5. which unresolved prime correlations appear if they do not.

Possible endings are all acceptable:

- **known + sufficient:** plug the theorem into a finite extremal/inertia problem;
- **known + too weak:** clean negative;
- **Hardy–Littlewood wall again:** write down exactly where it reappears and stop.

That is now the actual gamble.

## Why higher moments are tempting — and why the wall is real

Claude's paper explicitly identifies higher Gram moments as a conditional route to stronger constants. Under a Hardy–Littlewood-type higher-correlation input, fourth-order information gives `13/18 ≈ 72.22%` simple on-line zeros; sufficiently rich moment information drives that counting mechanism toward 100% simple/on-line zeros, still without proving RH.

Unconditionally, higher-order correlation is restricted by arithmetic support. `Gosh` therefore needs an analytic support accounting, not another RMT-looking numerical experiment.

## Stop lines

- the **same latent zero/block configuration** feeds every aperture;
- off-line reflected/conjugate blocks are represented explicitly;
- no random-matrix average replaces a worst-case inequality;
- no numerical zero data substitutes for a prime-side theorem;
- unconditional and Hardy–Littlewood-conditional inputs stay separate;
- toy `sum theta` is never silently identified with the theorem's Fourier support;
- if the useful mixed fourth moment requires exactly the unresolved correlation already named in Claude's paper, record the wall rather than renaming it.

## Related PerceptionLab repos

- `AnttisBrain2` — four-bounce resolution horizon.
- `HorizonNet` — correction: horizon belongs to the observer / decision margin.
- `HilbertPolyaReintepretation` — prime loops / trace-log / closed-walk language; its realizability lemma remains the cliff.
- `Alkuluku` — generic RMT statistics are cheap; arithmetic prime structure must survive the representation.
- `Nuoli` — Hermitian broken-time-reversal mechanics can produce GUE statistics without solving the arithmetic problem.

## Ledger

**Known mathematics being reused:** approximate functional equations, Riemann–Siegel truncation, Neumann/Fredholm expansions, Weyl perturbation, Sylvester inertia, restricted-support n-level correlation, mixed test functions, Gram trace moments.

**Verified here:** raw fixed-depth zeta contraction fails; a determinant contraction horizon degenerates at its zero; spectral-margin truncation can freeze inertia; homometric configurations defeat all pair-distance information while higher closed-walk moments distinguish them; under a fixed toy aperture budget, asymmetric fourth-order allocation can be substantially more discriminative than equal allocation.

**Not verified:** that the useful mixed higher moment is unconditionally available on the zeta prime side; that it yields a stronger worst-case inertia inequality; any improved zero proportion.

**Forbidden headline:** `four terms approximate the Riemann zeta function`.

---

*Gosh is allowed to be a silly repo. Its controls are not allowed to be silly.*
