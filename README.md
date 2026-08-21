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
            └── next target: joint multi-aperture certificate
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

There is no fixed contraction factor below one, and `sum_p p^-1/2` is not absolutely convergent. A universal `four terms = infinity` rule is therefore unavailable. Approximate functional equations / Riemann–Siegel are the legitimate number-theory version of a finite horizon, and their depth grows with height.

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

For Hermitian `G`, if a truncation `G_K` has a rigorous tail bound

```text
||G - G_K||_op <= delta_K
```

and

```text
min_j |lambda_j(G_K)| > delta_K,
```

Weyl perturbation says the omitted tail cannot move an eigenvalue through zero. The inertia is already fixed.

That is the spectral equivalent of `below one pixel`:

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

They have exactly the same multiset of pairwise distances. Consequently, for every even translation-invariant kernel, pair-level Gram information such as `tr(G)` and `tr(G^2)` cannot distinguish them at any bandwidth.

Using

```text
G_ij = sinc(theta * (x_i - x_j)),
```

that prediction holds to machine precision across the sweep. But higher traces — sums over closed triangles / longer walks — separate the configurations.

At `theta=0.4`:

```text
|Δ tr(G^2)|  ≈ 1.8e-15
|Δ tr(G^3)|  ≈ 0.19095
|Δ tr(G^4)|  ≈ 0.90291
```

So:

> **coarse higher-order information can contain something that even perfectly sharp pair-distance information cannot contain, because a bag of edges does not specify how those edges assemble into closed walks.**

This is the useful connection to the old Hilbert–Pólya / prime-loop language: `tr(G^k)` is a closed-walk sum.

## Important prior-art correction

`higher moment -> narrower Fourier support` is **not a new principle**. Restricted-support n-level correlation is established territory, especially Rudnick–Sarnak. Claude's own higher-moment discussion sits against that arithmetic support wall.

The experiment therefore does **not** claim a new bandwidth law. What survives is only the architectural question:

> **Can a sharp pair-level compression and a coarser higher-order compression constrain the same zero configuration jointly?**

The homometric result shows such a combination is not information-theoretically redundant. It does not show that number theory supplies the required higher moment or that the two matrices can legally be combined in one inequality.

## Why higher moments are tempting — and why the wall is real

Claude's paper explicitly identifies higher Gram moments as a conditional route to stronger constants. Under a Hardy–Littlewood-type higher-correlation input, fourth-order information gives `13/18 ≈ 72.22%` simple on-line zeros; sufficiently rich moment information drives that counting mechanism toward 100% simple/on-line zeros, still without proving RH.

Unconditionally, higher-order correlation is restricted by arithmetic support. So `Gosh` is not trying to calculate one more empirical moment. The next gate has to answer whether information at **different apertures** can meet in a valid worst-case certificate.

# Next target — the joint multi-aperture certificate

Let one common zero / block configuration `Z` generate two Hermitian compressions:

```text
G_sharp(Z)    # large bandwidth, pair-level arithmetic known
G_coarse(Z)   # narrower bandwidth, candidate higher moment
```

The next legitimate question is whether there exists a configuration-wise inequality combining quantities such as

```text
tr(G_sharp), tr(G_sharp^2), tr(G_coarse^2), tr(G_coarse^4)
```

that forces more on-line/simple structure than the sharp pair certificate alone.

This must be attacked first on finite synthetic zero/off-line block configurations. If no joint inequality helps there, stop before doing any analytic number theory.

### Stop lines

- the **same latent configuration** must feed every aperture;
- off-line reflected/conjugate blocks must be represented explicitly;
- no random-matrix average may replace a worst-case inequality;
- no numerical zero data may substitute for a prime-side theorem;
- unconditional and Hardy–Littlewood-conditional inputs stay separate;
- if the useful fourth moment requires exactly the unresolved correlation already named in Claude's paper, record the wall rather than renaming it.

## Related PerceptionLab repos

- `AnttisBrain2` — source of the four-bounce resolution-horizon observation.
- `HorizonNet` — the correction: horizon belongs to the observer / decision margin.
- `HilbertPolyaReintepretation` — prime loops / trace-log / closed-walk language; its realizability lemma remains the cliff.
- `Alkuluku` — generic RMT statistics are cheap; arithmetic prime structure must survive the representation.
- `Nuoli` — Hermitian broken-time-reversal mechanics can produce GUE statistics without solving the arithmetic problem.

## Ledger

**Known mathematics being reused:** approximate functional equations, Riemann–Siegel truncation, Neumann/Fredholm expansions, Weyl perturbation, Sylvester inertia, restricted-support n-level correlation, Gram trace moments.

**Verified here:** raw fixed-depth zeta contraction fails; a determinant contraction horizon degenerates at its zero; spectral-margin truncation can freeze inertia; homometric configurations defeat all pair-distance information while contracted higher closed-walk moments distinguish them.

**Not verified:** that the useful higher moment is unconditionally available on the prime side; that multiple apertures admit a stronger common inertia certificate; any improved zeta-zero proportion.

**Forbidden headline:** `four terms approximate the Riemann zeta function`.

---

*Gosh is allowed to be a silly repo. Its controls are not allowed to be silly.*
