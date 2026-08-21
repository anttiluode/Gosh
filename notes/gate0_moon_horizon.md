# Gate 0 — The Moon Horizon Meets a Zero

## Question

`AnttisBrain2` rendered an apparently infinite recursive hall of mirror moons with four bounces because the repeated bounce operator contracted both amplitude and visible spatial scale. `HorizonNet` later sharpened the lesson: **the useful horizon is set by what the observer can still distinguish, not by a mystical property of the number four.**

The evening question was deliberately naive:

> Could the same idea help with Riemann / infinite series?

The answer after Gate 0 is:

> **Not as a fixed truncation of zeta. Possibly as a finite-to-certificate rule for Hermitian/inertia objects. And the most interesting transplant may be multiscale: deeper trace information at deliberately lower arithmetic bandwidth.**

That is enough of a surviving object to continue, but the naive version is dead.

---

## 0A — Why `4 = infinity` does not transfer to the critical-line series

For the Dirichlet terms on the critical line,

\[
a_n(t)=n^{-1/2-it},
\]

we have

\[
\frac{|a_{n+1}|}{|a_n|}=\sqrt{\frac{n}{n+1}}\to 1.
\]

There is no uniform contraction factor `rho < 1` that makes the raw tail geometrically disappear. The prime amplitudes `p^{-1/2}` are not absolutely summable either.

So the literal transplant

```text
zeta = first four terms + invisible tail
```

is false.

The experiment records the term ratio climbing from `0.953` at `n=10` to `0.9999995` at `n=10^6`, and the absolute prime sum `sum_{p<=X} p^-1/2` keeps growing. This is not subtle; it is the correct immediate kill.

Analytic number theory already has its own legitimate observation horizons. The approximate functional equation / Riemann–Siegel machinery replaces an infinite representation near height `t` by a finite main sum of rough length

\[
N\sim \sqrt{t/(2\pi)}
\]

plus a controlled remainder / dual contribution. Gate 0 logs the rough lengths `3, 39, 398, 398942` at heights `10^2,10^4,10^6,10^12`. The horizon exists, but it grows with the requested arithmetic height. Four is not universal.

**Verdict 0A: killed.**

---

## 0B — The Fredholm / Neumann version hits the zero wall exactly

A more sophisticated transplant is operator-theoretic. Suppose some construction writes a relevant analytic object as

\[
D(s)=\det(I-L_s)
\]

for a trace-class operator `L_s`.

Whenever

\[
\|L_s\|<1,
\]

we get the familiar Neumann horizon

\[
(I-L_s)^{-1}=\sum_{m\ge0}L_s^m,
\]

with tail bound

\[
\left\|\sum_{m>K}L_s^m\right\|
\le
\frac{\rho^{K+1}}{1-\rho},
\qquad \rho=\|L_s\|<1.
\]

Likewise, a trace-log expansion can be controlled in a contraction region.

But

\[
D(s)=0
\]

means `I-L_s` is not invertible. For compact / trace-class `L_s`, this means `1` lies in the spectrum of `L_s`, hence its spectral radius is at least one. Therefore the very condition that gives the moon-style geometric horizon fails at the spectral point we want to detect.

The toy makes the wall literal with

\[
L_\rho=\operatorname{diag}(\rho,0.2),
\qquad
\det(I-L_\rho)=0.8(1-\rho).
\]

For an error target `1e-6`, the certified Neumann depth is:

| rho | required K |
|---:|---:|
| 0.2 | 8 |
| 0.5 | 20 |
| 0.8 | 69 |
| 0.9 | 152 |
| 0.99 | 1832 |
| 0.999 | 20712 |
| 1.0 | no geometric certificate |

As the determinant approaches zero, the horizon runs away; at the zero it disappears.

This is almost exactly the lesson `HorizonNet` learned in another domain: a contraction certificate is strongest once the interesting dynamics have already settled. It can certify a zero-free / invertible region; it cannot by itself walk through the singular event.

**Verdict 0B: useful negative. A pure contraction proof engine does not breach the Riemann wall.**

---

## 0C — Put the horizon in the certificate, not in the series

The surviving version uses the observer instead of the internal dynamics.

Let `G` be Hermitian and suppose we have a computable truncation `G_K` with a rigorous operator-norm tail bound

\[
\|G-G_K\|_{op}\le\delta_K.
\]

Weyl perturbation gives

\[
|\lambda_j(G)-\lambda_j(G_K)|\le\delta_K
\]

for every ordered eigenvalue.

Therefore, if

\[
\min_j |\lambda_j(G_K)| > \delta_K,
\]

no omitted term can push an eigenvalue through zero. The inertia of `G` is already fixed by `G_K`.

This is the exact spectral analogue of the moon renderer:

```text
AnttisBrain2: omitted image structure < one pixel
Gosh:        omitted operator tail < eigenvalue sign margin
```

The toy infinite Hermitian series is deliberately generic — no zeta content is smuggled into it. It uses terms with a known geometric norm envelope. The long reference sum has eigenvalues

```text
[-0.419630, 0.470481, 1.005620, 1.676182]
```

and inertia

```text
(negative, zero, positive) = (1, 0, 3).
```

The rigorous tail bound first falls below the computed sign margin at `K=2`; every certified truncation has the same inertia as the long reference.

This is not surprising mathematics — it is Weyl's theorem used as an observation horizon — but it is the right transplant of the AnttisBrain idea. **The number four vanishes; the decision margin survives.**

**Verdict 0C: mechanism works generically. No Riemann content established.**

---

# The unexpected seam with Claude's 2026 result

The current Anthropic / Alpöge–Furman work is exactly about extracting arithmetic consequences from a finite Hermitian compression of Weil's form, using trace/Frobenius information and Sylvester inertia to control off-line pairs.

That makes inertia a legitimate `observer` for the horizon idea.

But there is a second fact in the paper that matters more.

Its discussion of higher moments says that, at the full prime range `X ~ T`, available unconditional arithmetic estimates do not supply the higher trace moments needed to improve the method. The paper phrases the relevant range schematically as

\[
X^k \lesssim T^{2-\varepsilon}.
\]

At `X ~ T`, this leaves only the lowest moment regime. The same discussion says that under a Hardy–Littlewood-type higher-correlation hypothesis, fourth-order information would raise the simple-on-line lower bound to

\[
13/18 \approx 0.7222,
\]

and sufficiently many such moments would drive the method toward 100% simple zeros on the line (while still not proving RH itself).

So the obstruction after Claude is not `there are infinitely many terms` in a generic sense. It is more specific:

> **higher spectral information asks for arithmetic correlations at a range current unconditional number theory cannot supply.**

That is a much better wall to attack.

---

# Gate 1 candidate — contracting bandwidth with moment depth

The AnttisBrain translation now suggests something concrete instead of mystical:

> **Do not ask deeper trace moments to retain full arithmetic resolution. Contract the bandwidth as the moment order rises.**

If the available range is roughly

\[
X^k\le T^{2-\varepsilon},
\]

then define an arithmetic aperture schedule

\[
X_k = T^{\theta_k},
\qquad
k\theta_k < 2.
\]

For example, higher `k` gets deliberately smaller `theta_k`. This is structurally the same move as the mirror moons:

```text
bounce depth rises  -> spatial resolution contracts
moment order rises  -> arithmetic bandwidth contracts
```

The question is not whether this computes the same full-bandwidth moment. It does not. The question is:

> **Can sharp low-order/full-bandwidth information plus blurrier higher-order information certify more inertia / more simple on-line zeros than the full-bandwidth two-moment certificate alone?**

That is Gate 1.

## Registered stop lines for Gate 1

1. **No fake information.** A lower-bandwidth higher moment must be derivable from unconditional prime-side estimates in the claimed range. We do not numerically substitute actual zeros for a prime-side theorem.
2. **No comparing unlike matrices silently.** `G_{theta=1}` and `G_{theta<1}` are different compressions. Any joint certificate has to state explicitly why information from both can constrain the same zero configuration.
3. **No GUE proxy.** Better random-matrix-looking statistics are irrelevant unless the certificate becomes configuration-wise stronger.
4. **No hidden Hardy–Littlewood assumption.** If the joint moment requires the same unresolved prime correlations as the full-bandwidth higher moment, Gate 1 is dead.
5. **A numerical separation is only reconnaissance.** Even if multiscale moments distinguish synthetic configurations that Claude's first moments do not, the repo must derive a valid inequality before calling it mathematical progress.

---

# Current ledger

### Verified in Gate 0

- Raw critical-line terms do not support a fixed geometric contraction horizon.
- A Neumann contraction horizon degenerates as an operator determinant approaches a zero.
- A Hermitian *decision-space* horizon is rigorous: operator-tail bound below spectral sign margin freezes inertia.

### Existing mathematics, not ours

- Approximate functional equations / Riemann–Siegel truncation.
- Neumann series and Fredholm determinant theory.
- Weyl eigenvalue perturbation and Sylvester inertia.
- Transfer-operator / determinant techniques in dynamical zeta theory.
- Claude / Alpöge–Furman's 2026 rank–trace method and its stated higher-moment barrier.

### New only as a research question

The proposed **multiscale moment schedule** — use progressively narrower arithmetic bandwidth for progressively higher trace order, then combine those compressions in one configuration-wise certificate — is currently just a question. No novelty claim and no theorem.

---

## Reproduce Gate 0

```bash
pip install numpy
python experiments/gate0_horizon_wall.py
```

Receipt: `results/gate0_horizon_wall.json`.

---

*The moons did not solve an infinite series. They reminded us to ask what the observer actually needs. For Riemann, the observer may be inertia; the wall may be arithmetic bandwidth.*
