# Gosh

An intentionally silly name for a serious falsification workflow around Riemann-adjacent ideas.

> **This repository does not claim a proof of the Riemann Hypothesis.**
>
> The rule is the same as the better PerceptionLab repos: turn an intuition into a small mathematical gate, register what would kill it, and keep the negative result if it dies.

## Why this repo exists

The immediate prompt came from two otherwise unrelated lines:

1. **Claude / Alpöge–Furman (August 2026):** the new rank–trace / inertia argument proving that more than two thirds of zeta zeros are simple and on the critical line. Its structural move is to turn prime-side trace information into a constraint on how many negative directions the zero side can contain.
2. **AnttisBrain2 / HorizonNet (July 2026):** an apparently infinite hall of mirror moons became observationally complete after four bounces because one repeated operator contracted both amplitude and visible resolution. HorizonNet later clarified the important lesson: the useful horizon belongs in the *observer/decision*, not automatically in the internal state.

The question for `Gosh` is therefore not "can four terms solve an infinite zeta series?" They cannot. The question is:

> **Can an observation-horizon argument make an infinite operator / trace construction finite-to-certificate, without throwing away the arithmetic information that matters?**

That wording gives the idea somewhere precise to fail.

## Branch map

```text
main
│
└── sol/gate0-moon-horizon
      Gate 0A  raw-series contraction test              KILLED
      Gate 0B  Fredholm / Neumann zero-wall             VERIFIED NEGATIVE
      Gate 0C  certificate-space spectral horizon       WORKS IN TOY
      │
      └── next: sol/gate1-contracting-bandwidth
            deeper moment -> narrower arithmetic aperture
```

## Gate 0 — verdict

Branch: [`sol/gate0-moon-horizon`](../../tree/sol/gate0-moon-horizon)

Detailed note: [`notes/gate0_moon_horizon.md`](../../blob/sol/gate0-moon-horizon/notes/gate0_moon_horizon.md)

Experiment: [`experiments/gate0_horizon_wall.py`](../../blob/sol/gate0-moon-horizon/experiments/gate0_horizon_wall.py)

Receipt: [`results/gate0_horizon_wall.json`](../../blob/sol/gate0-moon-horizon/results/gate0_horizon_wall.json)

### 0A — raw zeta / prime series: killed

On the critical line,

```text
|a_(n+1)| / |a_n| = sqrt(n/(n+1)) -> 1.
```

There is no uniform geometric contraction factor below one, and the prime amplitudes `p^-1/2` are not absolutely summable. A universal fixed-depth `4 = infinity` truncation is therefore not available. Analytic number theory already has the legitimate version — approximate functional equations / Riemann–Siegel — whose required depth grows with height.

### 0B — Fredholm / Neumann horizon: useful negative

If

```text
D(s) = det(I - L_s)
```

and `||L_s|| < 1`, a Neumann / trace-log tail can be certified geometrically. But `D(s)=0` means `1` is in the spectrum of `L_s`, so the contraction condition fails at the zero itself.

The toy makes the failure visible. For an error target `1e-6`, the required Neumann depth rises

```text
rho=.8   -> K=69
rho=.9   -> K=152
rho=.99  -> K=1832
rho=.999 -> K=20712
rho=1    -> no geometric certificate
```

So a pure contraction certificate can certify invertible / zero-free regions; it cannot by itself cross the spectral event of interest.

### 0C — the surviving transplant: horizon in certificate space

Let a Hermitian target be `G`, a computed truncation be `G_K`, and suppose

```text
||G - G_K||_op <= delta_K.
```

By Weyl perturbation, every eigenvalue moves by at most `delta_K`. If

```text
min_j |lambda_j(G_K)| > delta_K,
```

the omitted tail cannot change any eigenvalue sign. The inertia is already certified.

This is the exact analogue of the moon renderer's `below one pixel` rule:

```text
AnttisBrain2: uncomputed image < visual resolution
Gosh:         uncomputed operator < spectral sign margin
```

In the deterministic infinite Hermitian toy the certificate fires after only `K=2` terms and all certified truncations have the same inertia as a 200-term reference. **Four disappears; the observation-margin principle survives.**

This is standard perturbation theory used in a particular role, not a Riemann result.

## The more interesting wall found after Gate 0

Claude's paper already discusses higher Gram / trace moments. At full arithmetic bandwidth, the known unconditional prime estimates do not supply the higher correlations needed to exploit those moments. The paper records a schematic range of the form

```text
X^k <= T^(2-epsilon).
```

At `X ~ T`, higher order rapidly leaves the unconditional range. Conditionally, the paper shows why those moments matter: a Hardy–Littlewood-type fourth-order input would lift the simple-on-line proportion to `13/18 ≈ 72.22%`, while sufficiently many moments drive this counting mechanism toward 100% simple on-line zeros (still not RH).

That changes the target. The obstacle is not generic infinity; it is **arithmetic resolution versus moment depth**.

## Gate 1 candidate — contracting arithmetic bandwidth

The AnttisBrain-shaped gamble is now:

```text
mirror bounce gets deeper -> spatial resolution contracts
trace moment gets higher  -> arithmetic bandwidth contracts
```

Choose a schedule

```text
X_k = T^theta_k,     k * theta_k < 2,
```

so deeper moments stay inside an unconditional analytic range. Then ask:

> **Can sharp low-order/full-bandwidth information plus blurrier higher-order information constrain the same zero configuration more strongly than the bandwidth-one two-moment certificate?**

This is not yet a theorem or novelty claim. A valid Gate 1 must explain how the different-bandwidth Hermitian compressions constrain the *same* zero configuration and must not smuggle in the very Hardy–Littlewood correlations it claims to avoid.

### Gate 1 stop lines

- no numerical zero data substituted for a prime-side theorem;
- no silent comparison of different matrices / bandwidths;
- no GUE-looking-spectrum proxy;
- no hidden Hardy–Littlewood assumption;
- numerical separation is reconnaissance only until a configuration-wise inequality exists.

## Related PerceptionLab repos

- `AnttisBrain2` — source of the four-bounce resolution-horizon observation.
- `HorizonNet` — the correction: the useful horizon is tied to the observer / decision margin.
- `HilbertPolyaReintepretation` — prime loops / trace-log / delay-network language; its Prime Orbit Condition + self-adjoint realizability lemma remains the cliff.
- `Alkuluku` — standing falsifier: generic RMT statistics are cheap; the arithmetic prime trace is the thing that must survive.
- `Nuoli` — broken time reversal can move a Hermitian construction from GOE toward GUE without making its spectrum complex; necessary symmetry mechanics, not the arithmetic solution.

## Ledger

**Known mathematics being reused:** approximate functional equations, Riemann–Siegel truncation, Neumann series, Fredholm determinants, trace-log expansions, Banach contraction bounds, Weyl eigenvalue perturbation, Sylvester inertia, Gabor / band-limited compressions.

**Verified here:** the raw moon-style truncation fails; the contraction horizon degenerates at a determinant zero; a decision-space spectral-margin horizon can rigorously freeze inertia in a toy infinite Hermitian sum.

**Current hypothesis:** progressively coarser arithmetic apertures may make some higher-order spectral information unconditional and jointly useful. Unchecked.

**Forbidden headline:** "four terms approximate the Riemann zeta function".

---

*Gosh is allowed to be a silly repo. Its controls are not allowed to be silly.*
