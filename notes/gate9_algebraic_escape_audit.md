# Gate 9 — Algebraic jumps are real, but they are not free

## Why this gate exists

Gate 8 ended with one deliberately narrow question:

> Is there a genuinely discontinuous/algebraic zero-side invariant, other than inertia, that distinguishes an arbitrarily small off-line displacement from the double-zero limit and is still cheaply visible from the prime side?

The obvious candidates are rank, nullity, determinants, principal minors and characteristic-polynomial coefficients.

They are worth checking because Gate 8 showed a mismatch:

```text
classification:
  a = 0     -> on line
  a != 0    -> off line

bounded analytic matrix observation:
  H(a) = H(0) + O(a^2).
```

A discontinuous algebraic invariant might, in principle, jump even when the matrix entries converge smoothly.

It does.

The problem is that the jump is not a free low-bandwidth observable.

No RH claim is made here.

---

## 9A — the local determinant really is an exact detector

Reuse the exact Gate-8 toy

```text
u(a) = [1, 1+i a].
```

The reflected-pair block is

```text
H(a)
 = u(a)u(a)^T + conjugate(u(a))conjugate(u(a))^T
 = 2 [[1, 1],
      [1, 1-a^2]].
```

Therefore

```text
det H(a) = -4 a^2.
```

So:

```text
a = 0      -> det H = 0, rank 1,
a != 0     -> det H < 0, rank 2 with one negative direction.
```

This is exactly the kind of algebraic jump Gate 8 left open.

Rank and determinant can distinguish every nonzero displacement, however tiny, **when the zero-side block is known exactly**.

For a general reflected block

```text
H(a)=2(x x^T-y y^T),
```

put

```text
D = ||x||^2 ||y||^2 - (x dot y)^2.
```

The product of its two possible nonzero eigenvalues is

```text
lambda_+ lambda_- = -4D.
```

With the Gate-8 analytic expansion

```text
x(a)=v0+O(a^2),
y(a)=a v1+O(a^3),
```

we get generically

```text
D = a^2 ||v0||^2 ||v1_perp||^2 + O(a^4),
```

hence

```text
det_on_span(H(a))
 = -4 a^2 ||v0||^2 ||v1_perp||^2 + O(a^4).
```

So the determinant version and the negative-eigenvalue version are the same local geometry viewed through different spectral coordinates.

---

## 9B — exact algebraic discontinuity does not remove the observation horizon

The determinant itself is exact, but the matrix received from a finite-bandwidth / approximate prime-side computation is not.

For a Hermitian matrix, the smallest operator perturbation that can move a simple eigenvalue to zero has norm equal to the magnitude of that eigenvalue.

In the Gate-8 toy,

```text
lambda_-(a)
 = 2-a^2-sqrt(4+a^4)
 = -a^2+O(a^4).
```

Let `v_-` be its normalized eigenvector and perturb by

```text
E0 = |lambda_-| v_- v_-^T.
```

Then

```text
H(a)+E0
```

lies exactly on the rank boundary. A perturbation only 1% larger pushes that eigenvalue positive and flips the determinant from negative to positive.

The experiment records

```text
||E0||_op / a^2 -> 1.
```

So rank/determinant do not evade Gate 8's Weyl horizon. They only restate it sharply:

> **an exact algebraic invariant can jump at a=0, but certifying the jump from an approximate matrix still requires error smaller than the O(a^2) spectral gap.**

There is no contradiction between exact rank and finite observational resolution.

---

## 9C — global minors are exterior-power moments, not a secret cheap statistic

Perhaps the local determinant is fragile, but a determinant or collection of minors of the **whole** Gram compression might carry the needed exact information in a different way.

For an `n x n` matrix `G`, let

```text
p_k = tr(G^k)
```

and let `e_k` be the `k`th elementary symmetric polynomial of the eigenvalues. Equivalently,

```text
e_k = tr(ExteriorPower^k G).
```

Newton's identities give

```text
k e_k = sum_{j=1}^k (-1)^(j-1) e_(k-j) p_j.
```

Thus

```text
e1      needs p1,
e2      needs p1,p2,
e3      needs p1,p2,p3,
...
det(G)=en needs p1,...,pn.
```

So the characteristic polynomial is not an algebraic escape from the higher-moment ladder. It is another basis for the same spectral-polynomial information.

The Gate-1 homometric attacker makes this visible with no asymptotics.

For

```text
A={0,1,4,10,12,17},
B={0,1,8,11,13,17},
G_ij=sinc(.4(x_i-x_j)),
```

we obtain

```text
Delta e1 = 0
Delta e2 = 0
Delta e3 = 0.0636503083
Delta e4 = 0.1561753856
Delta e5 = 0.1146599120
Delta e6 = 0.0234808486
```

and `e6=det(G)` agrees with the direct determinants.

The first two algebraic spectral coefficients tie for exactly the same reason the first two trace moments tie: homometry fixes the pair information. The first new elementary invariant appears only when `tr(G^3)` is allowed to enter.

That is the same closed-walk / correlation-order wall in different coordinates.

This does **not** prove that every imaginable discontinuous invariant is useless. It closes the standard finite-dimensional spectral-polynomial family:

```text
rank / determinant / characteristic coefficients / exterior powers
```

as a free route around the moment hierarchy.

---

## 9D — an important frontier correction: pair information was not actually exhausted

The earlier gates correctly killed a specific route:

```text
smoothed scalar L2
 -> one translation-invariant nonnegative pair kernel
 -> one linear bandwidth-one form-factor certificate.
```

But while this branch was being developed, public follow-up work on the 2026 Alpöge–Furman / Anthropic framework made an important distinction impossible to ignore.

`ainta/zeta-simple-zeros` keeps the **local Gram geometry** instead of compressing everything to one scalar pair functional. It adds a stability defect

```text
Delta(M)=tr Psi(M)
```

and derives finite 3-point / 7-point inequalities from the same bandwidth-one overlap kernel. Its public proof/reproducer reports a bound

```text
0.673008527927...
```

above the original Montgomery–Taylor / Anthropic constant

```text
0.672500703679...
```

without invoking unrestricted higher correlations.

Reference:

- https://github.com/ainta/zeta-simple-zeros

A later public candidate, `trmdy/zeta-simple-zeros-673137`, reports

```text
0.673312742272...
```

with finite certificates, while explicitly marking the strengthened theorem as pending expert review and end-to-end formalization.

Reference:

- https://github.com/trmdy/zeta-simple-zeros-673137

The lesson for `Gosh` is important:

> **pair-level arithmetic is not the same thing as a single linear form-factor statistic.**

Local arrangement, several pair values used jointly, convex spectral defects and configuration-wise inequalities can retain information that a single averaged pair functional throws away.

So Gates 5–7 should be read narrowly and correctly: they kill particular pair projections and two-moment summaries, not every possible use of bandwidth-one pairwise kernel data.

---

## 9E — Gate 8 independently landed on the current off-line-pair frontier

The most interesting collision is in that later campaign's second-stage notes.

It identifies an **off-line pair bridge** as the main possible route beyond its pure simple-zero pair-energy method. The proposed move is:

```text
off-line hyperbolic pair
        |
        v
virtual on-line double
```

while retaining the pair's interaction with the surrounding Gram defect, or else charging a spectral penalty.

That is essentially the geometry Gate 8 derived independently:

```text
off-line reflected pair a -> 0
        |
        v
multiplicity-2 on-line block,
H(a)=H(0)+O(a^2).
```

The external campaign reports a very instructive split:

**survives locally**

- exact complex pair-block formulas;
- one-pair bridge inequalities in a positive environment;
- safe regrouping that preserves the simple-zero defect.

**fails globally in naive form**

- additive pricing of several off-line pairs;
- generic PSD composition;
- several natural Schur / shifted-kernel assemblies.

Its remaining conjectural step is kernel-specific: exploit the fact that the actual Gram matrix comes from translates of a **positive-type bandlimited kernel**, rather than from an arbitrary PSD matrix.

Reference:

- https://github.com/trmdy/zeta-simple-zeros-673137/blob/main/docs/campaign-2.md

So the pair-to-double observation in Gate 8 should **not** be presented as a novelty claim. It is parallel convergence onto a live 2026 frontier.

That is good news scientifically: the route was not just an internally pretty metaphor. Another independent attack, starting from the strengthened zero-counting machinery rather than AnttisBrain/Clockfield, arrived at the same object because the algebra forced it there.

---

## 9F — where the remaining low-bandwidth question now lives

After this audit, the next question is no longer

```text
find a cleverer exact invariant.
```

Rank and determinant already give the obvious exact jump, and they inherit the same `a^2` robustness threshold. Global characteristic data merely repackages the higher-moment hierarchy.

The live question is narrower and more concrete:

> **Can the special positive-type / bandlimited structure of the actual Weil–Gram kernel make the virtual-double bridge compose globally, even though the corresponding statement is false for arbitrary PSD matrices?**

That question is attractive for three reasons:

1. it stays inside the actual bandwidth-one arithmetic interface rather than asking immediately for Hardy–Littlewood-strength higher correlation;
2. generic matrix theory is already known to be insufficient, so any positive result would have to use real analytic structure of the kernel;
3. Gate 8 supplies the local small-`a` geometry and the exact quadratic degeneration that any bridge theorem has to respect.

A sensible next gate would therefore reproduce a **minimal two-pair / multi-pair virtual-double composition problem using the actual optimized overlap kernel**, register the known counterexamples to naive addition, and test a taxed or regularized spectral defect that is designed to survive the `a -> 0` boundary.

Do not start by optimizing constants. First reproduce the bridge algebra and the failures.

---

## Verdict

Gate 9 gives a clean answer to Gate 8's last abstract loophole.

```text
exact local rank/determinant jump              YES
robust under finite matrix error uniformly     NO: margin ~ a^2
whole-matrix determinant as cheap alternative  NO: it packages moments up to order n
pair arithmetic completely exhausted           NO: local/joint pair geometry can do more
most interesting surviving route               kernel-specific off-line-pair bridge
```

So the repo should not end with “finite resolution cannot see RH.” That would be too strong.

The better boundary is:

> **continuous magnitude observables lose an arbitrarily near-line pair quadratically; exact algebraic observables can still classify it, but making that exact classification available from bandwidth-one prime-side data appears to require either higher spectral/correlation order or a kernel-specific global composition theorem.**

That is a much narrower wall, and now it touches the actual 2026 research frontier.
