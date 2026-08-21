# Gate 5 — Make L2 admissible and see what survives

## Question

Gate 4 found an exact identity

```text
L2(Xi;t) / Xi(t)^2
  = sum_{j<k} 1/((t-z_j)^2 (t-z_k)^2),
```

so the normalized second Laguerre layer is a pure two-zero interaction.

That looked arithmetically attractive, because restricted-support two-level correlation is available unconditionally in regimes where fourth-order information is not.

The catch was that the normalized pair kernel has poles at the zeros. This gate asks what happens when we make the object admissible.

The answer is a trilemma:

1. **exact/local L2 geometry** is regular only because `Xi^2` cancels the pair-kernel poles;
2. **entire bandlimited pair probes** can be built with rigorous tails, but a uniform construction over every possible zeta zero requires strong smoothing;
3. once those probes are averaged into translation-invariant pair information, the Gate-1 homometric attacker and the Alpöge–Furman bandwidth-one pair ceiling return.

No RH progress is claimed.

---

## 5A — an entire bandlimited Poisson/curvature probe

Use the shifted second-pole combination

```text
K_eta(u) = 1/(u-i eta)^2 + 1/(u+i eta)^2
         = 2 (u^2-eta^2)/(u^2+eta^2)^2.
```

With Fourier convention `hat f(xi)=∫f(u)e^{-2 pi i xi u}du`,

```text
hat K_eta(xi) = -4 pi^2 |xi| exp(-2 pi eta |xi|).
```

Truncate the Fourier integral at physical bandwidth `B`:

```text
K_eta,B(z)
  = ∫_{-B}^{B} -4 pi^2 |xi| e^{-2 pi eta |xi|} e^{2 pi i xi z} dxi.
```

Because the Fourier support is compact, `K_eta,B` is entire of exponential type `2 pi B`.

If `|Im z| <= d < eta`, then

```text
|K_eta(z)-K_eta,B(z)|
 <= 8 pi^2 ∫_B^infinity xi e^{-2 pi (eta-d) xi} dxi
 = 8 pi^2 e^{-alpha B} (B/alpha + 1/alpha^2),
alpha = 2 pi (eta-d).
```

Define the dimensionless horizon variable

```text
x = 2 pi (eta-d) B.
```

Multiplying the tail bound by the natural pole scale `(eta-d)^2` gives

```text
(eta-d)^2 * tail_bound <= 2 (x+1) e^{-x}.
```

So the same observation-horizon law appears again: **bandwidth times analytic-strip margin** is the variable that controls when omitted frequencies stop mattering.

Representative values:

```text
x=.1  -> 1.99064
x=.5  -> 1.81959
x=1   -> 1.47152
x=2   -> .812012
x=4   -> .183156
x=8   -> .0060383
x=12  -> .00015975
```

This is a rigorous tail bound, not a claim about sign preservation. Sign/inertia still needs a decision margin.

---

## 5B — zeta supplies an analytic strip margin, but only asymptotically

Write the zero coordinate used on the zero side as

```text
z_rho = gamma - i(beta-1/2).
```

Every nontrivial zero lies in `0<beta<1`, so `|Im z_rho|<1/2`.

Mossinghoff–Trudgian–Yang prove the explicit Vinogradov–Korobov zero-free region

```text
beta <= 1 - 1/[55.241 (log |gamma|)^(2/3) (log log |gamma|)^(1/3)]
```

for `|gamma|>=3`; by the functional equation the same margin holds at the left edge. Thus in a height window one may take

```text
d <= 1/2 - m(T),
m(T) = 1/[55.241 (log T)^(2/3)(log log T)^(1/3)]
```

up to the usual care about using the worst height in the window.

If we place the smoothing poles at `eta=1/2`, the analytic margin is at least `m(T)`.

Under the standard local-zero scaling, a normalized Fourier support `sigma` corresponds to physical frequency of order

```text
B ~ sigma log T / (2 pi).
```

Then

```text
x = 2 pi m(T) B
  ~ sigma * (log T)^(1/3) / [55.241 (log log T)^(1/3)],
```

which tends to infinity for every fixed `sigma>0`.

So a fixed normalized support can, **asymptotically**, make this smoothed probe's Fourier tail arbitrarily small even uniformly over the allowed critical strip.

Two warnings are load-bearing:

1. the explicit constant makes the convergence fantastically slow; this is an asymptotic structural statement, not a practical numerical one;
2. `eta=1/2` is a very strong smoothing of the exact `1/u^2` Laguerre kernel. This proves admissibility of a related probe, not approximation of exact `L2/Xi^2` in a norm strong enough to preserve its sign.

Reference: M. Mossinghoff, T. Trudgian, A. Yang, *Explicit zero-free regions for the Riemann zeta-function*, arXiv:2212.06867.

---

## 5C — the uniform-approximation obstruction is conceptual, not numerical

To approximate the singular kernel `1/u^2` itself by the shifted pair `K_eta`, one wants `eta -> 0`.

To keep the Fourier representation uniformly controlled at **every possible off-line zero coordinate**, one needs

```text
eta > sup |Im z_rho|,
```

which is essentially `eta >= 1/2` without RH-type information.

Those requirements point in opposite directions.

The zero-free region improves the strict margin `eta-d`, so it makes Fourier truncation of a fixed smoothed probe certifiable. It does **not** make `eta` small.

Therefore the legal bandlimited object is not automatically a faithful surrogate for the exact normalized Laguerre statistic.

This is the first Gate-5 wall.

---

## 5D — averaging makes the arithmetic cheap and the information pair-level

Suppose a bandlimited atom `K_B(t-z_j)` is used and we average a quadratic quantity over the center coordinate `t`. Ignoring edge taper for the schematic identity,

```text
∫ K_B(t-z_j) conjugate(K_B(t-z_k)) dt
```

is an autocorrelation kernel depending only on `z_j-z_k`.

On the Fourier side its multiplier is

```text
|hat K_B(xi)|^2,
```

so the resulting zero statistic is a **linear functional of the pair form factor**.

That is precisely why the arithmetic becomes cheap: it has been projected into pair information.

It also means the Gate-1 homometric attacker returns. For any translation-invariant pair kernel `r`, the two configurations

```text
A={0,1,4,10,12,17}
B={0,1,8,11,13,17}
```

have identical

```text
sum_{j,k} r(x_j-x_k).
```

The experiment in this branch verifies the tie for autocorrelation kernels generated by several `(eta,B)` choices.

So smoothing + center averaging repairs admissibility at the price of discarding the connected higher-order information Gate 1 had exposed.

---

## 5E — the Alpöge–Furman pair ceiling is now an explicit attacker

The Lean artifact's `PairCeiling` theorem is not a vague statement about two moments. It constructs a 256-periodic law of marked configurations with simple-point fraction

```text
p0 = 0.68182868746...
```

and form factor essentially equal to the CUE/GUE pair law throughout normalized bandwidth one.

For **every** sufficiently smooth bandwidth-one weight `r` for which a proposed certificate is valid against that law,

```text
c0 + sum_j s_j r(j/256) <= p,
```

the theorem bounds the corresponding continuum certificate by `p0` plus explicit edge/variation terms.

See:

- `anthropics/zeta-23-lean/Zeta23/PairCeiling/CeilingLaw256.lean`
- `.../PairCeiling/Stability.lean`
- `.../PairCeiling/LawN256.lean`

The law is made from marked configurations with multiplicities `m_i in {1,2}` totaling 256, so it is directly designed to attack simple-point certificates while matching bandwidth-one pair data.

This gives a precise escape criterion for any regularized `L2` proposal:

> after all necessary smoothing and averaging, can its configuration-wise certificate be written as `c0 + integral r d(form factor)` with support inside one?

If **yes**, it is in the PairCeiling attack class. Calling the kernel `Laguerre` does not buy new information.

If **no**, identify exactly what survives beyond the form factor — for example absolute center dependence, a nonlinear use of several pair observables, or a genuinely connected higher-order term — and then ask whether the prime side supplies that extra object unconditionally.

Gate 5 does not yet prove which side the best `L2` construction falls on, because the missing step is not algebra. It is the **configuration-wise inequality that turns a regularized L2 observable into a bound on simple/on-line zeros**.

---

## The trilemma

The current map is now unusually sharp:

```text
EXACT LOCAL L2
  regular and sensitive because Xi^2 cancels singularities
  but not a bare admissible pair-correlation test
        |
        | normalize / expose pair structure
        v
SINGULAR TWO-ZERO KERNEL
  algebraically only pair order
  but poles at the zeros
        |
        | smooth + bandlimit + average
        v
LEGAL PAIR / FORM-FACTOR OBSERVABLE
  unconditional restricted-support arithmetic available
  but homometric blindness + PairCeiling attack return
        |
        | retain connected higher-order information instead
        v
HIGHER CORRELATION
  informative in Gate 1/2
  but arithmetic support / Hardy–Littlewood wall returns
```

That is a much more useful wall than `Riemann is hard`.

## Verdict

Claude's statement `L2 may be arithmetically cheaper than tr(G^4)` is **true in one precise sense**:

- normalized `L2` has only two-zero combinatorics;
- an admissible smoothed/averaged descendant can live in two-level arithmetic.

But there is no free fourth-order information hiding inside that cheapness. Every legal step toward ordinary pair-correlation arithmetic risks projecting the observable back into exactly the pair-information class that the 2026 bandwidth-one ceiling was built to defeat.

## Next gate

The only question worth asking next is not `try another kernel`.

Take one concrete smoothed `L2` candidate and derive a **configuration-wise simple-zero inequality** from it. Then classify the resulting certificate:

```text
A. linear bandwidth-one form-factor certificate -> PairCeiling catches it;
B. outside PairCeiling but prime-side unconditional -> genuinely interesting;
C. outside PairCeiling and needs higher prime correlation -> same arithmetic wall, now located exactly;
D. cannot preserve sign/inertia under smoothing -> observation-horizon route dies before arithmetic.
```

Any of those is a good result.