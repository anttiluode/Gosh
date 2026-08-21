# Gate 8 — An off-line pair becomes a double on-line zero

## Why this gate exists

Gate 7 left one possible low-support loophole:

> perhaps the off-line hyperbolic block itself carries a local sign/inertia constraint that is stronger than ordinary pair form-factor information, even when we do not use higher matrix moments.

There is such structure — exact inertia can distinguish an arbitrarily small off-line displacement — but its **magnitude** has a hard observation horizon.

The key limit also explains why the Alpöge–Furman bandwidth-one adversary is built from multiplicity-2 points.

---

## 8A — the zero-side pair block

For one off-line reflected pair, let `a=beta-1/2` be the transverse displacement from the critical line. The evaluation vector of a real-entire test family can be written

```text
u(a) = x(a) + i y(a),
```

with

```text
u(-a) = conjugate(u(a)).
```

The pair contribution to the real-symmetric/Hermitian zero-side matrix is

```text
H(a)
 = u(a)u(a)^T + conjugate(u(a))conjugate(u(a))^T
 = 2 [x(a)x(a)^T - y(a)y(a)^T].
```

This is exactly the hyperbolic decomposition used in the 2026 zero-side argument.

---

## 8B — analyticity forces quadratic approach to a double zero

If the component test functions are analytic and real on the real axis, their Taylor expansion gives

```text
u(a) = v0 + i a v1 - a^2 v2/2 - i a^3 v3/6 + ...,
```

with real vectors `v0,v1,...`. Therefore

```text
x(a) = v0 - a^2 v2/2 + O(a^4),
y(a) = a v1 - a^3 v3/6 + O(a^5).
```

Substitution gives

```text
H(a)
 = 2 v0 v0^T
   - a^2 [v0 v2^T + v2 v0^T + 2 v1 v1^T]
   + O(a^4).
```

Hence

```text
||H(a)-H(0)|| = O(a^2).
```

But

```text
H(0)=2 v0 v0^T
```

is precisely what two coincident on-line zeros contribute — equivalently, one critical-line zero of multiplicity 2.

So:

> **a reflected off-line pair tends quadratically, as a matrix observable, to a double zero on the line.**

The marked double points in the PairCeiling law are not an arbitrary unrelated pathology. They sit on the boundary of the same zero-side block geometry.

---

## 8C — the negative eigenvalue also disappears quadratically

Let

```text
H=2(xx^T-yy^T).
```

Put

```text
A = ||x||^2 - ||y||^2,
D = ||x||^2 ||y||^2 - (x dot y)^2 >= 0.
```

The two possible nonzero eigenvalues are

```text
lambda_+/- = A +/- sqrt(A^2 + 4D).
```

If

```text
x=v0+O(a^2),
y=a v1+O(a^3),
```

then

```text
D = a^2 ||v0||^2 ||v1_perp||^2 + O(a^4),
```

and, generically,

```text
lambda_- = -2 a^2 ||v1_perp||^2 + O(a^4).
```

If `v1` happens to be parallel to `v0`, the first negative term can occur at still higher order. Either way there is **no uniform positive lower bound** on the magnitude of the negative direction as `a -> 0`.

Exact inertia is discontinuous enough to notice `lambda_-<0` for every nonzero `a`. A finite-accuracy matrix approximation is not.

---

## 8D — the Weyl observation horizon

Suppose the prime-side/finite-bandwidth matrix is known only up to operator error

```text
||E||_op <= delta.
```

Weyl perturbation can certify the negative direction only if

```text
|lambda_-(a)| > delta.
```

With the generic quadratic law this requires

```text
a^2 * sensitivity > delta,
```

or schematically

```text
a > sqrt(delta / sensitivity).
```

This is Gate 0 again, now attached directly to the off-line block.

The mathematical index can jump at `a=0`; an approximate observation of the matrix cannot resolve that jump below its spectral sign margin.

---

## 8E — an exact two-channel toy

Take the analytic evaluation vector

```text
u(a) = [1, 1+i a].
```

Then

```text
x=[1,1],
y=[0,a],
```

and

```text
H(a)=2 [[1,1],
        [1,1-a^2]].
```

At `a=0`,

```text
H(0)=2 [[1,1],
        [1,1]],
```

the rank-one block of a double on-line atom.

The difference is exact:

```text
||H(a)-H(0)||_op = 2 a^2.
```

The eigenvalues are

```text
lambda_+/- = 2-a^2 +/- sqrt(4+a^4),
```

so

```text
lambda_- = -a^2 + O(a^4).
```

The experiment checks this down to `a=1e-5`; `|lambda_-|/a^2 -> 1` and the matrix difference divided by `a^2` is exactly 2 up to floating precision.

---

## 8F — why this matters differently for two targets

### Simple-on-line zeros

An off-line reflected pair is bad for the target `simple and on the line`.

Its `a=0` limit is a **double** on-line zero, which is also bad for that target.

So the target itself is continuous under this degeneration: bad pair -> bad double point. This is why a marked multiplicity-2 law is such a natural pair-information adversary for simple-zero certificates.

### Merely on-line zeros / RH

For the target `is the zero on the critical line?`, the classification *does* jump at `a=0`: every nonzero `a` is off-line, however tiny, while `a=0` is on-line.

Any bounded-bandwidth continuous matrix observable approaches the on-line block as `O(a^2)`. Therefore a magnitude-based finite-resolution certificate cannot uniformly separate `a=0` from arbitrarily small `a!=0` without some additional gap information.

This does not prove RH inaccessible to every method. It says this particular continuous finite-observation strategy cannot turn a quantitative block magnitude into an exact on-line/off-line classifier without resolving an arbitrarily small sign.

---

## 8G — what remains of the hyperbolic-block loophole

There is still a distinction between **index** and **magnitude**.

The 2026 argument already exploits index: every off-line pair gives a hyperbolic block with at most one positive direction, independent of how weak that direction is. That is powerful precisely because it does not require a lower bound on `|a|`.

A proposed improvement based on *how negative* or *how curved* the block is faces the quadratic-collapse problem above.

To beat it one would need one of:

1. a zeta-specific lower bound on transverse displacement of off-line zeros — none is known and such a statement would itself be very strong;
2. a discontinuous/exact algebraic invariant accessible from the prime side, not merely an approximate matrix magnitude;
3. an aggregate theorem showing enough off-line zeros cannot all sit below the resolution horizon;
4. higher-order arithmetic information that detects the coalescence pattern differently.

Options 3–4 are again arithmetic questions, not kernel engineering.

## Verdict

Gate 8 explains the geometry behind several previous failures:

```text
off-line pair a != 0
       |
       | a -> 0, quadratic in observed matrix
       v
multiplicity-2 on-line point
```

For simple-zero certification, the PairCeiling marked double is the natural closure of the off-line block.

For RH-style on-line certification, the exact distinction lives in a sign whose magnitude can shrink like `a^2`, so Gate 0's spectral-margin horizon is unavoidable for finite-bandwidth approximations.

This does not open a route past the Riemann wall. It tells us why the remaining low-support loophole is much narrower than it looked.