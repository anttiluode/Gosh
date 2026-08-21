# Gate 3 — The valley has depth

## ClockfieldRiemann is useful, but not for its old headline

`ClockfieldRiemann` originally stated that the critical line being a transverse valley floor for `|xi|^2` was equivalent to RH. Fable's later audit, `the_valley_has_a_name.md`, corrected this sharply:

- the central differential identity is correct;
- the first valley condition is the classical first **Laguerre inequality** for `Xi(t)=xi(1/2+it)`;
- RH implies it;
- the converse does not follow from that one inequality, and Fable supplied explicit xi-like counterexamples with off-line zeros for which the first valley condition still holds;
- the full generalized Laguerre hierarchy, not merely the first inequality, is the classical real-zero / Laguerre-Polya criterion.

That correction is exactly what makes the repo useful to `Gosh`.

The relevant classical identity is

```text
|f(x+i y)|^2 = sum_{n>=0} L_n(f;x) y^(2n).
```

For the Riemann Xi function,

```text
Xi(t) = xi(1/2+i t),
xi(1/2 + a + i t) = Xi(t - i a),
```

so

```text
|xi(1/2+a+i t)|^2 = sum_{n>=0} L_n(Xi;t) a^(2n).
```

The generalized Laguerre expressions are therefore literally the successive **transverse Taylor coefficients of the Clockfield valley**.

`L_1` is the old curvature observable:

```text
L_1 = Xi'(t)^2 - Xi(t) Xi''(t),
```

and

```text
d^2/da^2 |xi(1/2+a+i t)|^2 at a=0 = 2 L_1.
```

So Clockfield did not discover an RH equivalence. It accidentally selected the first pixel of an already-known infinite resolution ladder.

References to check before any novelty language:

- Csordas, Varga, Vincze (1990), *Jensen polynomials with applications to the Riemann xi-function*.
- Csordas, Ruttan, Varga (1991), *The Laguerre inequalities with applications to a problem associated with the Riemann hypothesis*.
- Csordas, Vishnyakova (2013), *The generalized Laguerre inequalities and functions in the Laguerre-Polya class*.
- Wang, Yang (2024), *Laguerre inequalities and complete monotonicity for the Riemann Xi-function and the partition function*.

Nothing in this branch claims that the Laguerre hierarchy is new.

---

## Gate 3A — Fable's own attacker is caught one level deeper

Fable's strip-interior counterexample can be written in the Xi variable as

```text
f(z) = cos(k z) (z^2 + a^2),
k = pi/0.8,
a = 0.4.
```

It has a dense real-zero background from `cos(kz)` and one conjugate nonreal pair `z=+- i a`, corresponding to an off-critical-line pair in the xi variable.

Fable showed numerically that `L_1(x)>0` throughout the tested interval even though the nonreal pair is present. Gate 3 reproduces that scan on `[0,40]` with step `0.001`:

```text
min L_1 = 0.0747841760 at x=0.
```

Now look one transverse order deeper. At `x=0`,

```text
|f(i y)|^2 = cosh^2(k y) (a^2-y^2)^2.
```

Writing `q=(a k)^2` gives exactly

```text
L_1(0) = a^2 (q-2),
L_2(0) = q^2/3 - 2q + 1.
```

For Fable's parameters,

```text
a k = pi/2,
q   = 2.46740110027,
L_1(0) = +0.0747841760,
L_2(0) = -1.9054461373.
```

So the counterexample that kills the first-valley equivalence is itself killed immediately by the next Laguerre layer.

This is not surprising in hindsight: all orders are the real-zero criterion. But it makes the old Clockfield geometry useful again because it tells us what "deeper transverse resolution" actually means mathematically.

---

## Gate 3B — there is no universal finite Laguerre depth in the toy

The same family also shows why `four = infinity` cannot simply be moved from ray bounces to Laguerre order.

At the symmetry point the sign of `L_n` depends only on

```text
q = (a k)^2.
```

For `n>=3`, after removing a positive coefficient,

```text
sign L_n(0) = sign R_n(q),
R_n(q) = 1 - 8q/B + 16q^2/(A B),
A = (2n)(2n-1),
B = (2n-2)(2n-3).
```

The negative interval is bounded by

```text
q_(n,+/-) = [A +/- sqrt(A(8n-6))]/4.
```

Its center is approximately `n^2`, so the order at which the hidden conjugate pair becomes visible is naturally of scale

```text
n ~ sqrt(q) = a k.
```

The numerical first-failure scan at `x=0` is:

```text
ak= 1.571 -> first negative order  2
ak= 2.449 -> first negative order  3
ak= 3.162 -> first negative order  3
ak= 4.472 -> first negative order  4
ak= 7.071 -> first negative order  6
ak=10.000 -> first negative order  9
ak=14.142 -> first negative order 13
ak=22.361 -> first negative order 20
ak=31.623 -> first negative order 29
```

This is only a local synthetic family. It does **not** establish that the global first failing Laguerre inequality for Xi has this scaling. But it gives a clean adversary to any proposal that a fixed finite order should generically certify all-real zeros.

The dimensionless variable `a k` is suggestive: off-line displacement times background oscillation frequency. Fable's original explanation already said a denser real-zero background can hide an off-line pair from `L_1`. The higher-order calculation tells us how extra transverse orders begin to unhide it.

---

## Gate 3C — the Poisson observation horizon survives, with a correction

From the earlier curvature calculation for an off-line pair,

```text
C_a(u) = 4 (u^2-a^2)/(u^2+a^2)^2,
hat C_a(freq) = -8 pi^2 |freq| exp(-2 pi a |freq|).
```

Moving away from the critical line therefore applies the Poisson multiplier

```text
exp(-2 pi a |freq|).
```

For an observer bandlimited to `|freq|<=B`, the signature energy is proportional to

```text
E_B(a) = integral_0^B freq^2 exp(-4 pi a freq) d freq.
```

After `freq=B u`, every normalized quantity depends on the single product

```text
x = a B.
```

Claude proposed using

```text
1 - E_B(a)/E_B(0)
```

as "discrimination". The product collapse is correct, and for small `x`,

```text
1 - E_B(a)/E_B(0) = 3 pi x + O(x^2).
```

But this is **energy attenuation**, not a metric distance between the two signatures.

The actual normalized squared L2 distance is

```text
J(x) = ||C_0-C_a||_B^2 / ||C_0||_B^2
     = 3 integral_0^1 u^2 (1-exp(-2 pi x u))^2 du,
```

and therefore

```text
J(x) = (12 pi^2/5) x^2 + O(x^3).
```

So the useful statement is:

> finite-bandwidth observability is controlled by `aB`, but the small-displacement law depends on what the observer measures.

A linear test functional can have first-order sensitivity; energy loss is linear here; squared metric separation is quadratic. Do not conflate them.

This is the mathematically honest version of the AnttisBrain resolution-horizon analogy.

---

## Gate 3D — Claude's Gate 2b edge-loading prediction is killed

Claude proposed that the Gate 2 mixed-aperture optimum should keep improving if two legs are pushed toward the whole support budget while the other two become nearly blind.

The direct attacker says no.

At fixed total toy budget `1.6`:

```text
(0.40,0.40,0.40,0.40) -> separation 0.902906
(0.70,0.05,0.70,0.15) -> separation 2.154172   # Gate 2 best on 0.05 grid
(0.78,0.02,0.78,0.02) -> separation 0.217089
(0.79,0.01,0.79,0.01) -> separation 0.039908
(0.80,0.00,0.80,0.00) -> separation ~7e-15
```

The extreme paired limit returns to a pair-level statistic and homometry kills it. The small legs are not disposable bookkeeping; they are part of the closed-walk interference that carries the extra information.

So the monotone single-leg Fourier weight does **not** determine the mixed four-leg optimum. Gate 2's asymmetric optimum remains an empirical property of that toy, not a consequence of "push everything to the edge".

---

## What ClockfieldRiemann actually adds to Gosh

Before this audit, `Gosh` had two loosely connected ideas:

```text
higher trace / closed walk depth
bandwidth / observation horizon
```

ClockfieldRiemann supplies a third, classical axis:

```text
transverse Laguerre depth.
```

The useful diagram is now

```text
                         SAME HIDDEN ZERO CONFIGURATION
                                   |
              +--------------------+--------------------+
              |                    |                    |
       Weil / Gram matrix     transverse Xi jet    Poisson-smoothed
       trace + inertia        L1, L2, L3, ...      curvature response
              |                    |                    |
       arithmetic support      all orders =          observer bandwidth
          is the wall          real-zero test          is the horizon
```

The two right-hand columns are not yet inputs to Alpoge-Furman's inertia inequality. That arrow remains the whole research question:

```text
finite / smoothed Laguerre information
                |
                v  ?
prime-side computable Hermitian constraint
                |
                v
stronger positive-index / simple-zero certificate
```

A likely failure mode is that `L_2,L_3,...` are nonlinear derivative combinations and obtaining them from prime-side information simply reintroduces the same higher-correlation arithmetic wall already seen in higher Gram moments. If so, write down that wall exactly and stop.

## Verdict

ClockfieldRiemann helps.

Not because the original equivalence claim survived — it did not.

It helps because Fable's correction reveals that the old valley picture was the first coefficient of a **known infinite hierarchy**, and that hierarchy gives `Gosh` a much better attacker against the original "finite observation of infinity" intuition.

The question is no longer "can four see infinity?"

It is:

> **what finite spectral / arithmetic information is sufficient to certify enough of an infinite real-zero hierarchy, and what adversary hides just beyond that information horizon?**

That is still Riemann-adjacent reconnaissance, not progress on RH.
