# Gate 6 — The safe L2 certificate collapses to pair correlation

## Result up front

Gate 5 left one concrete task: derive a **configuration-wise simple-zero inequality** from a legal smoothed L2-like probe and then see whether it lies inside the Alpöge–Furman bandwidth-one ceiling class.

For the safest construction, the answer is yes.

The route is exact and short.

---

## 6A — start with any bandlimited atom

Let `K_B` be any real bandlimited atom with

```text
supp(hat K_B) subset [-B,B].
```

The Gate-5 Poisson/curvature atom is one example, but the argument below does not depend on its special formula.

Build the nonnegative physical-space kernel

```text
R_B(u) = |K_B(u)|^2 >= 0.
```

Its Fourier transform is the autocorrelation/convolution

```text
hat R_B = hat K_B * conjugate-reflect(hat K_B),
```

so

```text
supp(hat R_B) subset [-2B,2B].
```

Therefore `B<=1/2` keeps the resulting pair certificate inside normalized bandwidth one.

---

## 6B — multiplicity gives a simple-point certificate

Take a real marked point configuration with distinct locations `x_i`, multiplicities `m_i>=1`, total multiplicity

```text
N = sum_i m_i,
```

and let `S` be the number of simple points (`m_i=1`).

Define

```text
Q_B = sum_{i,j} m_i m_j R_B(x_i-x_j).
```

Because `R_B` is pointwise nonnegative,

```text
Q_B >= R_B(0) * sum_i m_i^2.
```

For every multiplicity,

```text
m_i^2 >= m_i                 if m_i=1,
m_i^2 >= 2 m_i               if m_i>=2.
```

Hence

```text
sum_i m_i^2 >= S + 2(N-S) = 2N-S.
```

Combining the two inequalities gives the configuration-wise bound

```text
S/N >= 2 - Q_B/[N R_B(0)].
```

For the `{1,2}` marked configurations used by the PairCeiling adversarial law, `sum m_i^2 = 2N-S` exactly. The only slack is then the off-diagonal nonnegative contribution of `R_B`.

This is a real certificate, not an average or random-matrix heuristic.

---

## 6C — Fourier transform: it is exactly a form-factor certificate

Let

```text
F(alpha) = |sum_i m_i exp(2 pi i alpha x_i)|^2 / N
```

be the normalized form factor.

Fourier inversion gives

```text
Q_B/N = integral hat R_B(alpha) F(alpha) d alpha,
R_B(0) = integral hat R_B(alpha) d alpha.
```

Therefore

```text
S/N >= 2
       - [integral hat R_B(alpha) F(alpha) d alpha]
         /[integral hat R_B(alpha) d alpha].
```

Equivalently,

```text
2 + integral r(alpha) F(alpha) d alpha <= S/N,

r(alpha) = -hat R_B(alpha)/R_B(0).
```

This is precisely the architecture attacked by `Zeta23/PairCeiling`:

```text
c0 + integral r d(form factor) <= simple fraction.
```

If `2B<1`, the weight is supported strictly inside bandwidth one, so the troublesome endpoint terms at `alpha=1` vanish. For a reasonable smooth/tapered atom the derivative-variation term in the formal stability theorem is finite as well.

The fact that the kernel originated from `L2`, Poisson smoothing, or Clockfield geometry has disappeared. The certificate sees only the pair form factor.

---

## 6D — why the 0.6818 ceiling is a genuine adversary here

The Alpöge–Furman Lean artifact constructs a 256-periodic law of marked real configurations with

```text
m_i in {1,2},
sum_i m_i = 256,
simple-point fraction p0 = 0.68182868746...,
```

whose bandwidth-one form factor is essentially the CUE/GUE pair law.

`PairCeiling/CeilingLaw256.lean` proves that for every sufficiently regular bandwidth-one weight `r`, **if** a certificate

```text
c0 + sum_j s_j r(j/256) <= p
```

is valid against that law, then its continuum value is at most `p0` plus explicit boundary/variation slack.

Our inequality above is valid configuration-by-configuration for every real marked configuration, so in particular it is valid against every configuration in that law. Thus a smoothed-L2 certificate of this nonnegative-pair form is in the exact class the ceiling was designed to attack.

This does **not** say every conceivable use of `L2` is capped. It says the obvious safe route is.

---

## 6E — the toy receipt

The experiment uses the Gate-5 bandlimited Poisson atom with `eta=.5`, normalized atom bandwidth `B=.4`, hence pair bandwidth `.8<1`.

For marked configurations with multiplicities in `{1,2}`, it verifies

```text
actual simple fraction >= 2 - Q_B/[N R_B(0)].
```

On a separated example with marks

```text
[1,1,1,2,2,2]
```

the actual simple fraction is `1/3`. As the point spacing grows and off-diagonal kernel terms vanish, the bound approaches `1/3`:

```text
spacing  2  -> bound -0.112019
spacing  5  -> bound  0.330913
spacing 10  -> bound  0.333177
spacing 20  -> bound  0.333323
spacing 50  -> bound  0.33333308
```

This is exactly what the algebra predicts: for `{1,2}` marks the multiplicity inequality is tight, and only off-diagonal pair mass creates slack.

---

## What died

The hope was:

```text
L2 is fourth transverse order
but only two-zero combinatorics
therefore perhaps it gives richer information at pair-correlation cost.
```

For the safe nonnegative-kernel construction, the last implication is false.

It gives pair-correlation cost because it has become **only pair-correlation information**.

That is the same lesson as Gate 1 from a completely different direction.

---

## What remains open

An L2 route can escape this negative only by refusing at least one step above.

It must retain something such as:

1. **absolute center dependence** rather than averaging to a difference kernel;
2. **several pair observables used nonlinearly/jointly**, not one linear form-factor functional;
3. **sign-indefinite local information** whose cancellations encode off-line geometry;
4. a direct **Hermitian matrix/block construction** from transverse derivatives rather than a scalar pair certificate.

Each escape has a cost:

- if prime-side arithmetic cannot supply it unconditionally, the higher-correlation wall returns;
- if smoothing error can flip the relevant sign/inertia, the observation-horizon route dies first;
- if it can still be reduced to one bandwidth-one form-factor weight, PairCeiling catches it.

## Verdict

**Gate 6 is a clean negative.**

The most straightforward rigorous conversion of smoothed `L2` information into a simple-zero lower bound is mathematically just a Montgomery-style pair certificate and therefore sits inside the 2026 PairCeiling attack class.

This is useful because it explains *why* `L2` looked arithmetically cheap: the legal certificate had projected away the information that made higher Laguerre depth interesting.

The next worthwhile move, if any, is no longer `optimize the L2 kernel`. It is to ask whether the **local, sign-indefinite transverse block before nonnegative squaring** can be represented as a Hermitian matrix whose inertia is prime-side computable without collapsing to one pair form factor.