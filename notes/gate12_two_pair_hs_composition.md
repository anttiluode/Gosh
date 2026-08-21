# Gate 12 — The two-pair failure is not in the second moment

## Why this gate exists

The public August-2026 bridge campaign reports an exact actual-kernel **two-pair** counterexample to naive additive local pricing. At the same time, Gate 11 rewrote every reflected pair in terms of the analytic overlap kernel.

That lets us ask a much narrower question:

> Does virtualizing off-line pairs already fail at the raw Hilbert--Schmidt / second-moment level, or is the two-pair obstruction introduced later by the nonlinear stability defect and its spectral kink?

For two pairs, the raw second moment is safe.

In fact there are two exact composition statements:

```text
any number of pairs at a common transverse depth  -> HS-safe
any two pairs at arbitrary transverse depths      -> HS-safe
```

So the published two-pair bridge counterexample must live downstream of the second moment.

No RH or proportion improvement is claimed.

---

## 12A — exact cross interaction of two reflected pair blocks

Use Gate 11's normalized complex coordinate

```text
z_i = x_i - i D_i,
```

where `x_i` is the normalized ordinate and

```text
D_i = L(beta_i-1/2)/(2 pi).
```

Let

```text
u_i = u(z_i)
```

be the normalized full-lattice evaluation vector and

```text
H_i = u_i u_i^T + conjugate(u_i) conjugate(u_i)^T
```

its reflected-pair block.

Let the virtual on-line double at the same center be

```text
V_i = 2 u(x_i) u(x_i)^T.
```

Gate 11's complex Poisson identity gives

```text
u_i^T nu_j = k(z_i-z_j).
```

Put

```text
f(z)=k(z)^2.
```

Using

```text
tr[(a a^T)(b b^T)] = (a^T b)^2,
```

we get the exact cross term

```text
tr(H_i H_j)
 = 2 Re[
     f(x_i-x_j - i(D_i-D_j))
     +
     f(x_i-x_j - i(D_i+D_j))
   ].
```

For the virtual doubles,

```text
tr(V_i V_j)=4 f(x_i-x_j).
```

This is already enough to compute any full-lattice second-moment comparison without constructing the high-dimensional Gabor vectors.

---

## 12B — Bochner turns the whole problem into weighted Fourier sums

Because `k` is positive definite on the real axis, so is

```text
f=k^2.
```

By Bochner,

```text
f(x)=integral exp(2 pi i xi x) dmu(xi)
```

for a finite nonnegative even measure `mu`. For the bandlimited overlap kernel, `mu` is compactly supported.

Analytic continuation gives

```text
Re f(x-iA)
 = integral cos(2 pi xi x) cosh(2 pi xi A) dmu(xi).
```

Using

```text
cosh(a-b)+cosh(a+b)=2 cosh(a) cosh(b),
```

we obtain an exact global formula. For pair centers `x_i` and depths `D_i`,

```text
||sum_i H_i||_HS^2
 = 4 integral
     |sum_i c_i(xi) exp(2 pi i xi x_i)|^2
     dmu(xi),
```

where

```text
c_i(xi)=cosh(2 pi xi D_i) >= 1.
```

The fully virtualized doubles satisfy

```text
||sum_i V_i||_HS^2
 = 4 integral
     |sum_i exp(2 pi i xi x_i)|^2
     dmu(xi).
```

So raw pair composition becomes a very concrete question:

> does multiplying each Fourier phasor by a hyperbolic weight `c_i>=1` increase or decrease its squared resultant?

---

## 12C — common transverse depth is globally safe for any number of pairs

If

```text
D_i=D
```

for every pair, then at each frequency

```text
c_i(xi)=c(xi)
```

is common. Therefore

```text
|sum_i c exp(i theta_i)|^2
 = c^2 |sum_i exp(i theta_i)|^2
 >= |sum_i exp(i theta_i)|^2.
```

Integrating gives the exact theorem

```text
||sum_i H_i||_HS^2
 >=
||sum_i V_i||_HS^2
```

for **any number of reflected pairs at the same transverse depth** and arbitrary centers.

No spacing assumption is needed.

This is a kernel-specific positive-type statement of precisely the kind Gate 10 was looking for, but only at the raw second-moment level.

---

## 12D — two arbitrary depths are also globally safe

Now take only two pairs. At a fixed Bochner frequency write

```text
c1=cosh(2 pi xi D1),
c2=cosh(2 pi xi D2),
theta=2 pi xi(x1-x2).
```

The actual-minus-virtual integrand, omitting the common positive factor, is

```text
c1^2+c2^2-2 + 2(c1 c2-1) cos(theta).
```

Since

```text
c1 c2 >= 1,
```

the minimum over `theta` occurs at `cos(theta)=-1`. There it is

```text
(c1-c2)^2 >= 0.
```

Hence pointwise in frequency,

```text
|c1 e^{i theta1}+c2 e^{i theta2}|^2
 >=
|e^{i theta1}+e^{i theta2}|^2.
```

After integration:

> **For any two reflected off-line pairs, at arbitrary centers and arbitrary transverse depths, the full-lattice Hilbert--Schmidt energy is at least that of their two virtual on-line doubles.**

This is exact.

The experiment performs 20,000 random Montgomery--Taylor two-pair checks; the smallest observed difference is positive:

```text
min(actual HS - virtual HS) = 0.01087780015...
```

The numerical sweep is only a receipt; the inequality above is algebraic.

---

## 12E — why three unequal depths are qualitatively different

For three or more phasors, increasing their magnitudes individually need not increase the magnitude of their sum.

A frequency-level example is

```text
phases  = (0, 0, pi),
weights = (1.01, 1.01, 2).
```

Then

```text
unweighted |1+1-1|^2 = 1,
weighted   |1.01+1.01-2|^2 = 0.0004.
```

So the weighted-minus-unweighted integrand is

```text
-0.9996.
```

All three weights exceed one. Thus the two-pair proof cannot be extended to arbitrary many unequal depths merely from

```text
c_i>=1
```

and positivity of the Bochner measure.

This does **not** provide an actual Montgomery--Taylor integrated counterexample. It identifies the first algebraic place where a frequencywise positivity proof can fail.

Two special regimes remain exactly safe:

```text
m arbitrary, D_i all equal,

or

m <= 2, D_i arbitrary.
```

So any raw-HS obstruction requires at least three pairs **and** nonuniform transverse depth.

---

## 12F — this localizes the public two-pair bridge counterexample

The public campaign reports a certified actual-kernel two-pair failure for naive additive local pricing:

```text
delta_2 - 2 pi = -22.14
```

and separately reports a Schur-deficit witness and failure of generic PSD composition near the stability functional's eigenvalue-2 kink.

Reference:

- `trmdy/zeta-simple-zeros-673137`, `docs/campaign-2.md`.

Gate 12 does not contradict that counterexample. It says something useful about **where the failure cannot be**.

For two pairs,

```text
raw full-lattice second moment:
    actual >= virtual    [proved here]

naive additive bridge price:
    can fail             [public certified counterexample]
```

Therefore the loss must enter when the second-moment information is converted into the nonlinear stability/defect certificate, or when local pair prices are composed with the surrounding simple-zero Gram geometry.

That removes one possible culprit.

---

## 12G — the spectral kink is now the obvious target

The stability defect used by the current simple-zero refinement is

```text
Psi(lambda)
 = (lambda-1)^2,   0<=lambda<=2,
 = 2lambda-3,      lambda>=2.
```

The public campaign already identifies spectral crowding near `lambda=2` as the generic-PSD obstruction.

Gate 12 sharpens that diagnosis:

> the actual positive-type kernel can preserve the raw HS inequality for two arbitrary off-line pairs while the bridge still fails after applying the nonlinear spectral accounting.

So a future proof does not need to rescue the second moment for two pairs. It needs to control **how HS energy is redistributed across the eigenvalue-2 kink** when the hyperbolic pair blocks are coupled to the environment.

That suggests a better next variable than a spacing penalty:

```text
same trace
+ no two-pair HS loss
+ location of spectral mass relative to lambda=2.
```

In other words, the bridge is increasingly looking like a **spectral transport problem**, not an information-quantity problem.

---

## Verdict

Gate 12 proves a small but clean kernel-specific composition theorem:

```text
common depth, any number of pairs   -> raw HS virtualization safe
two pairs, arbitrary depths         -> raw HS virtualization safe
three+ unequal depths               -> pointwise proof can fail
```

The two-pair theorem is especially useful because a certified two-pair failure is already known for the *full bridge*. Therefore the obstruction is isolated downstream of raw pair energy.

The Riemann hypothesis remains untouched.

But the open lemma has become narrower again:

> **under the actual bandlimited positive-type kernel, can one control the transport of the guaranteed two-pair Hilbert--Schmidt surplus through the nonlinear defect kink at eigenvalue 2, rather than attempting to prove a nonexistent generic spectral gap?**

That is the question Gate 13 should answer or kill.
