# Gosh

An intentionally silly name for a serious falsification workflow around Riemann-adjacent ideas.

> **This repository does not claim a proof of the Riemann Hypothesis.**
>
> Turn an intuition into a small mathematical gate, register what would kill it, and keep the negative result when it dies.

`main` is the map. Derivations, experiments and receipts live on branches.

## Why this repo exists

Two lines collided:

- **Alpöge–Furman / Claude (August 2026):** prime-side trace information is converted into constraints on the inertia of a finite Hermitian zero-side compression, proving that more than two thirds of zeta zeros are simple and on the critical line.
- **AnttisBrain2 / HorizonNet:** an apparently infinite mirror recursion became finite-to-observer because deeper structure fell below a resolution threshold. HorizonNet later supplied the correction: a useful horizon belongs in the **observer / decision**, not automatically in the internal state.

The question is not `four terms = infinity`. It is:

> **Can infinite arithmetic / spectral structure become finite-to-certificate because the omitted information is too small or too coarse to change the decision?**

## Branch map

```text
main
│
├── sol/gate0-moon-horizon
│     raw zeta contraction                         KILLED
│     Fredholm/Neumann contraction at a zero       KILLED / ZERO WALL
│     spectral-margin inertia horizon              WORKS IN TOY
│
├── sol/gate1-contracting-bandwidth
│     homometric pair defeats all pair data        VERIFIED
│     coarse higher closed-walk moments separate   VERIFIED
│
├── sol/gate2-mixed-aperture-walks
│     mixed two-leg homometric control             TIES AS REQUIRED
│     fourth mixed walk separates                  VERIFIED
│     unequal allocation beats equal in toy        2.386x TOY GAIN
│
└── sol/gate3-laguerre-horizon
      Clockfield valley identified as L1            CLASSICAL / CORRECTED
      Fable L1-passing fake caught by L2            VERIFIED
      local Laguerre detection depth ~ a*k          SYNTHETIC TOY
      Poisson bandlimit depends on a*B               VERIFIED
      Gate2b extreme edge-loading extrapolation      KILLED
      Laguerre/Poisson -> AF inertia embedding        OPEN
```

---

# Gate 0 — the moons do not truncate zeta

Branch: [`sol/gate0-moon-horizon`](../../tree/sol/gate0-moon-horizon)

- [`notes/gate0_moon_horizon.md`](../../blob/sol/gate0-moon-horizon/notes/gate0_moon_horizon.md)
- [`experiments/gate0_horizon_wall.py`](../../blob/sol/gate0-moon-horizon/experiments/gate0_horizon_wall.py)
- [`results/gate0_horizon_wall.json`](../../blob/sol/gate0-moon-horizon/results/gate0_horizon_wall.json)

### Result

For the critical-line Dirichlet terms,

```text
|a_(n+1)| / |a_n| = sqrt(n/(n+1)) -> 1.
```

There is no universal AnttisBrain-style geometric contraction and no fixed `four = infinity` truncation.

A Fredholm/Neumann formulation also meets an exact wall: if

```text
D(s)=det(I-L_s)
```

vanishes, then `1` is in the spectrum of `L_s`; a uniform `||L_s||<1` certificate cannot survive at the zero it is meant to detect.

The surviving transplant is **decision-space truncation**. If

```text
||G-G_K||_op <= delta
```

and every computed eigenvalue of the Hermitian `G_K` is farther than `delta` from zero, Weyl perturbation freezes the inertia. The omitted infinity need not vanish; it merely cannot change the sign decision.

```text
AnttisBrain2: omitted image < one-pixel decision threshold
Gosh:         omitted operator < eigenvalue sign margin
```

Toy verdict: works; the accidental number four disappears.

---

# Gate 1 — pair information is not higher-order information

Branch: [`sol/gate1-contracting-bandwidth`](../../tree/sol/gate1-contracting-bandwidth)

- [`notes/gate1_contracting_bandwidth.md`](../../blob/sol/gate1-contracting-bandwidth/notes/gate1_contracting_bandwidth.md)
- [`experiments/gate1_contracting_bandwidth.py`](../../blob/sol/gate1-contracting-bandwidth/experiments/gate1_contracting_bandwidth.py)
- [`results/gate1_contracting_bandwidth.json`](../../blob/sol/gate1-contracting-bandwidth/results/gate1_contracting_bandwidth.json)

Attacker:

```text
A = {0,1,4,10,12,17}
B = {0,1,8,11,13,17}
```

These two sets are homometric: they have the same multiset of pairwise distances. Consequently every translation-invariant pair statistic ties at every bandwidth.

For

```text
G_ij = sinc(theta (x_i-x_j)),
```

at `theta=0.4`:

```text
|Δ tr(G^2)|  ~ 1.8e-15
|Δ tr(G^3)|  ~ 0.19095
|Δ tr(G^4)|  ~ 0.90291
```

A bag of edges does not specify how the edges assemble into closed walks.

### Prior-art stop line

`higher correlation order -> restricted Fourier support` is established analytic-number-theory territory. This gate claims only an information-theoretic toy result, not a new support theorem.

---

# Gate 2 — where the resolution is spent matters

Branch: [`sol/gate2-mixed-aperture-walks`](../../tree/sol/gate2-mixed-aperture-walks)

- [`notes/gate2_mixed_aperture_walks.md`](../../blob/sol/gate2-mixed-aperture-walks/notes/gate2_mixed_aperture_walks.md)
- [`experiments/gate2_mixed_aperture_walks.py`](../../blob/sol/gate2-mixed-aperture-walks/experiments/gate2_mixed_aperture_walks.py)
- [`results/gate2_mixed_aperture_walks.json`](../../blob/sol/gate2-mixed-aperture-walks/results/gate2_mixed_aperture_walks.json)

Use a mixed closed walk

```text
tr(G_t1 G_t2 G_t3 G_t4)
```

with the same hidden configuration feeding every factor.

All mixed two-leg traces still tie for the homometric attacker. At fixed toy aperture budget

```text
t1+t2+t3+t4 = 1.6,
```

equal allocation gives

```text
(.40,.40,.40,.40) -> 0.9029058562 separation,
```

while the `0.05` grid found

```text
(.70,.05,.70,.15) -> 2.1541721037 separation.
```

That is a `2.3858x` toy gain without increasing total aperture.

### Prior-art stop line

Unequal test functions / supports are known. What remains project-specific is only the proposed weld to the 2026 rank-trace/inertia architecture.

---

# Gate 3 — Clockfield's valley has an infinite depth coordinate

Branch: [`sol/gate3-laguerre-horizon`](../../tree/sol/gate3-laguerre-horizon)

- [`notes/gate3_laguerre_horizon.md`](../../blob/sol/gate3-laguerre-horizon/notes/gate3_laguerre_horizon.md)
- [`experiments/gate3_laguerre_horizon.py`](../../blob/sol/gate3-laguerre-horizon/experiments/gate3_laguerre_horizon.py)
- [`results/gate3_laguerre_horizon.json`](../../blob/sol/gate3-laguerre-horizon/results/gate3_laguerre_horizon.json)

This gate reopens [`anttiluode/ClockfieldRiemann`](https://github.com/anttiluode/ClockfieldRiemann), but uses Fable's later correction rather than the old headline.

The original valley condition is the first generalized Laguerre inequality for

```text
Xi(t)=xi(1/2+i t).
```

Classically,

```text
|f(x+i y)|^2 = sum_n L_n(f;x) y^(2n).
```

Since

```text
xi(1/2+a+i t)=Xi(t-i a),
```

the `L_n(Xi;t)` are literally the successive transverse coefficients of the old Clockfield landscape.

`L_1` is the valley curvature. The **whole** Laguerre hierarchy is the classical real-zero / Laguerre-Polya criterion. Therefore the old repo did not find a one-inequality RH equivalence; it independently landed on the first rung of an already-known infinite ladder.

## Gate 3A — Fable's counterexample passes L1 and fails L2

Fable's strip-interior attacker is

```text
f(z)=cos(kz)(z^2+a^2),
k=pi/0.8,
a=0.4.
```

It contains a nonreal pair `z=+-ia` but has positive first Laguerre difference over the tested real interval.

Gate 3 reproduces:

```text
min L1 on [0,40] = +0.0747841760.
```

At the symmetry point, with `q=(ak)^2`, the next coefficients are exact:

```text
L1(0)=a^2(q-2),
L2(0)=q^2/3 - 2q + 1.
```

For Fable's parameters:

```text
ak = pi/2
L1(0) = +0.0747841760
L2(0) = -1.9054461373
```

The counterexample that kills the first-valley equivalence is itself caught one transverse level deeper.

## Gate 3B — no fixed Laguerre depth in the synthetic family

For `n>=3`, the sign at the symmetry point depends only on `q=(ak)^2`:

```text
R_n(q)=1 - 8q/B + 16q^2/(A B),
A=(2n)(2n-1),
B=(2n-2)(2n-3).
```

The negative band is centered asymptotically near `q ~ n^2`, so the local detection order naturally scales like

```text
n ~ a k.
```

The receipt walks from first failure at order `2` for `ak=1.57` to order `29` for `ak=31.62`.

This is a synthetic local result, not a theorem about Xi. It is an attacker against any generic fixed-order `four = infinity` claim.

## Gate 3C — Poisson smoothing gives a real observation variable

For one off-line reflected pair the normalized log-curvature kernel has Fourier multiplier

```text
exp(-2 pi a |freq|).
```

With observer bandwidth `B`, normalized quantities collapse to the dimensionless product

```text
x = a B.
```

Claude's proposed

```text
1-E_B(a)/E_B(0)
```

has the correct small-`x` law

```text
3 pi x + O(x^2),
```

but it is **energy attenuation**, not a metric distance.

The actual normalized squared L2 distance between the `a=0` and `a>0` signatures is

```text
(12 pi^2/5) x^2 + O(x^3).
```

So `aB` is a genuine resolution coordinate, but different observers have different near-line sensitivity laws.

## Gate 3D — extreme edge loading dies

Claude predicted Gate 2 should improve further near two huge / two blind legs. It does not:

```text
(.70,.05,.70,.15) -> 2.154172
(.78,.02,.78,.02) -> 0.217089
(.79,.01,.79,.01) -> 0.039908
(.80,.00,.80,.00) -> ~7e-15
```

At the blind-leg limit the statistic collapses back to pair information and homometry wins. The tiny legs are part of the informative closed walk, not disposable slack.

---

# The open weld

We now have three views of the **same kind of hidden zero geometry**:

```text
Weil / Gram compression       -> traces, inertia, arithmetic support
transverse Xi expansion       -> L1, L2, L3, ...
Poisson curvature response    -> displacement x observer-bandwidth
```

What is **not** known in this project is the arrow that matters:

```text
finite / smoothed Laguerre or curvature information
                     |
                     v   ?
prime-side computable Hermitian constraint
                     |
                     v
stronger positive-index / simple-zero certificate
```

A likely death is that `L2,L3,...` require exactly the nonlinear/higher prime correlations that already block higher Gram moments. If so, the correct output is the exact missing arithmetic estimate, not another name for the wall.

## Next gate

No more pretty zero plots and no more aperture searches first.

Take **the lowest genuinely new Laguerre layer, `L2`**, and ask:

1. can a smoothed/localized `L2` observable be written in explicit-formula language;
2. what prime-side sums appear;
3. what Fourier support do they require;
4. are those sums unconditional in any useful support range;
5. can the resulting quantity constrain the same off-line `2m(xx^T-yy^T)` blocks used in the 2026 inertia proof?

If the answer dies at Hardy-Littlewood-type correlation, write that wall down and stop.

## Related repos

- `ClockfieldRiemann` — the old valley; Fable's audit relocates it to the first Laguerre inequality.
- `AnttisBrain2` — source of the resolution-horizon intuition.
- `HorizonNet` — correction: the horizon belongs to the observer/decision.
- `HilbertPolyaReintepretation` — closed-walk / trace-log language; realizability remains the cliff.
- `Alkuluku` — prime trace is the discriminator; generic RMT statistics are cheap.
- `Nuoli` — symmetry-class mechanics, not arithmetic.

## Standing stop lines

- no claim that the Laguerre hierarchy is new;
- no claim that `L1 >= 0` is equivalent to RH;
- no numerical zero data substituted for a prime-side theorem;
- no toy aperture budget silently identified with rigorous Fourier support;
- no random-matrix average substituted for a configuration-wise inequality;
- unconditional and Hardy-Littlewood-conditional inputs remain separate;
- no improved zeta-zero proportion is claimed until an end-to-end inequality exists.

---

*Gosh is allowed to be a silly repo. Its controls are not allowed to be silly.*
