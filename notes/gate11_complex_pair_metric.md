# Gate 11 — The two coalescence directions share one metric

## Why this gate exists

Gate 8 found a transverse boundary:

```text
off-line reflected pair, displacement a
          |
          | a -> 0
          v
double on-line zero
```

and showed that the negative spectral direction disappears quadratically.

Gate 10 found a longitudinal boundary:

```text
two nearby simple on-line atoms, separation d
          |
          | d -> 0
          v
double on-line atom
```

and showed that the simple-zero Gram eigenvalue approaches the defect threshold `2` quadratically.

Those looked like parallel local pictures. The complex Poisson--Gabor identity shows they are actually the **same overlap kernel viewed along its real and imaginary axes**.

This gate writes that coordinate relation explicitly.

No RH claim is made. The exact formulas below belong to the full Gabor lattice / limiting overlap-kernel model. The theorem uses a finite compression, so edge and tail errors have to be restored before any global arithmetic statement.

---

## 11A — the paper already gives the needed complex identity

For

```text
alpha_k = T + 2 pi k/L,
```

the 2026 Alpöge--Furman / Anthropic Poisson--Gabor lemma states, for **all complex** `z,z'`,

```text
sum_{k in Z} phihat(z-alpha_k) phihat(z'-alpha_k)
    = L * hat(phi^2)(z-z').
```

This is stronger than the real-only specialization used in the Lean proof of the on-line norm bound. The Lean source itself notes that the complex continuation is not needed there; the paper states it directly.

Reference:

- Levent Alpöge and Ralph Furman, *More than two thirds of the zeta zeros are simple and on the critical line*, arXiv:2608.13637, Lemma 2.1.

Normalize a full-lattice evaluation vector by

```text
u(z)_k = phihat(z-alpha_k) / sqrt(a L^2),
```

where

```text
a L = integral phi(u)^2 du.
```

Let

```text
k(z) = hat(phi^2)(2 pi z/L) / hat(phi^2)(0)
```

when using the dimensionless kernel coordinate below. The notation is chosen so that `k(0)=1` and, for real normalized separation `d`, `k(d)` is the ordinary overlap kernel used by the simple-zero Gram matrix.

---

## 11B — an off-line atom has fixed bilinear norm and enlarged Hermitian norm

Write a zero as

```text
rho = 1/2 + a + i gamma.
```

The paper's complex ordinate is

```text
gamma_rho = gamma - i a.
```

Introduce the dimensionless transverse displacement

```text
D = L a / (2 pi).
```

Set `z=gamma_rho`.

### Bilinear self-overlap

Take `z'=z` in the complex Poisson identity. Since `z-z'=0`,

```text
u(z)^T u(z) = 1.
```

This is exact on the full lattice and independent of `D`.

### Hermitian self-overlap

Because `phi` is real,

```text
conj(u(z)) = u(conj(z)).
```

Taking `z'=conj(z)` gives

```text
u(z)^* u(z)
 = k(2 i D)
 =: N(D).
```

For an even nonnegative spectral profile `v(t)` on `[-1/2,1/2]`, normalized to mass one,

```text
N(D)
 = integral v(t) cosh(4 pi D t) dt
   / integral v(t) dt.
```

Hence

```text
N(0)=1,
N(D)>1 for D!=0
```

unless the profile is degenerate at `t=0`.

The imaginary displacement does not alter the bilinear normalization. It increases the ordinary Hilbert-space norm.

---

## 11C — exact reflected-pair spectrum

Write

```text
u = x + i y,
```

with real vectors `x,y`.

From

```text
u^T u = 1
```

we obtain

```text
x dot y = 0,
||x||^2 - ||y||^2 = 1.
```

From

```text
u^* u = N(D)
```

we obtain

```text
||x||^2 + ||y||^2 = N(D).
```

Therefore

```text
||x||^2 = (N(D)+1)/2,
||y||^2 = (N(D)-1)/2.
```

The normalized contribution of the reflected pair is

```text
H(D)
 = u u^T + conjugate(u) conjugate(u)^T
 = 2 (x x^T - y y^T).
```

Since `x` and `y` are orthogonal, the two possible nonzero eigenvalues are **exactly**

```text
lambda_pair,+ = N(D)+1,
lambda_pair,- = -(N(D)-1).
```

At `D=0`,

```text
N(0)=1
```

and the spectrum becomes

```text
{2,0}.
```

That is the virtual multiplicity-two on-line atom.

So Gate 8's local statement can be sharpened in the full-lattice model:

> **the magnitude of the negative off-line direction is exactly the excess Hermitian norm `N(D)-1`.**

A public August-2026 follow-up campaign independently derives exact complex pair-block formulas and uses a scalar quantity of this kind in its attempted off-line-pair bridge. This gate should therefore be read as a reconciliation of `Gosh` with that frontier, not as a priority claim.

---

## 11D — real and imaginary motion have a universal 4:1 quadratic conversion

Let the normalized even spectral density have second moment

```text
mu2 = E[t^2].
```

For real normalized separation `d`,

```text
k(d) = E[cos(2 pi d t)].
```

Therefore

```text
1-k(d)
 = 2 pi^2 mu2 d^2 + O(d^4).
```

For transverse displacement `D`,

```text
N(D)
 = k(2 i D)
 = E[cosh(4 pi D t)],
```

so

```text
N(D)-1
 = 8 pi^2 mu2 D^2 + O(D^4).
```

Thus

```text
c_transverse / c_longitudinal = 4.
```

The ratio does **not** depend on the Montgomery--Taylor profile. It comes only from analytic continuation of the same even overlap kernel and the fact that a reflected pair spans `z-conj(z)=-2ia`.

Equivalently,

```text
transverse cost at D
      ~=
longitudinal crowding cost at d=2D
```

at leading quadratic order.

This is the cleanest relation yet between Gate 8 and Gate 10.

---

## 11E — Montgomery--Taylor numbers

For the limiting Montgomery--Taylor profile

```text
v(t)=cos(sqrt(2)t),    |t|<=1/2,
```

the experiment gives

```text
mu2 = 0.07749929632...
```

and therefore

```text
c_long = 2 pi^2 mu2
       = 1.5297747921...,

c_trans = 8 pi^2 mu2
        = 6.1190991684....
```

The numerical analytic continuation verifies the limits:

```text
x        (1-k(x))/x^2    (k(2ix)-1)/x^2    ratio
.1       1.52248          6.23712             4.09667
.03      1.52912          6.12963             4.00861
.01      1.52970          6.12027             4.00096
.003     1.52977          6.11920             4.00009
.001     1.52977          6.11911             4.00001
.0001    1.52977          6.11910             4.00000
```

And comparing the transverse penalty at `D` to the longitudinal penalty at `d=2D` gives ratio -> `1`.

---

## 11F — what this says about the virtual-double bridge

Gate 10 killed the hope for a universal spectral exclusion zone: ordinary on-line atoms can crowd arbitrarily close to the eigenvalue-2 boundary.

Gate 11 says that crowding is not an unrelated nuisance. Near a double atom, the two relevant departures are locally measured by the same spectral second moment:

```text
                    double atom
                        |
             -----------------------
             |                     |
      separate along line      leave the line
            d                     D
             |                     |
     cost ~ c d^2          cost ~ 4 c D^2
```

So if a global virtual-double theorem exists, a natural local accounting variable is not a hard spacing cutoff. It is a **quadratic exchange budget** between longitudinal separation and transverse displacement.

At the infinitesimal level,

```text
d^2 <-> 4 D^2.
```

This does not prove any global inequality. Multi-pair interference, finite-compression tails, multiplicities, and the nonlinear spectral defect still matter.

But it suggests a more constrained next experiment than generic anti-crowding:

> **Take the smallest actual-kernel configuration in which naive virtual-double addition fails, and ask whether the failure is controlled by a local charge built from `d^2-4D^2` (or its nonperturbative kernel version `1-k(d)` versus `k(2iD)-1`) plus the known Gram-defect pressure.**

That is testable and uses the exact kernel geometry rather than an invented penalty.

---

## 11G — finite-compression caveat

The exact identities above use the sum over every Gabor lattice point `k in Z`.

The actual zero-side matrix uses the finite range

```text
0 <= k < d.
```

The 2026 proof controls the omitted portion by the same tail machinery used for the trace and Hilbert--Schmidt estimates. Therefore it is legitimate to use the full-lattice formulas as the local limiting geometry, but **not** to silently replace a finite block by the exact two-eigenvalue model in a theorem.

A bridge proof would need a quantitative version:

```text
finite pair block
 = full-lattice pair geometry
 + controlled edge/tail error.
```

This is precisely where Gate 8's Weyl-margin warning returns.

---

## Verdict

Gate 11 does not improve the zeta-zero percentage and does not approach a proof of RH.

It does unify two pieces of `Gosh` that previously looked accidental:

```text
longitudinal simple-zero crowding
and
transverse off-line-pair collapse
```

are the real-axis and imaginary-axis responses of the **same analytic overlap kernel**.

The full-lattice identities are:

```text
u^T u = 1,
u^* u = k(2iD),

spec(pair) = { k(2iD)+1, -(k(2iD)-1) },

1-k(d)     ~ 2 pi^2 mu2 d^2,
k(2iD)-1   ~ 8 pi^2 mu2 D^2.
```

So the local conversion is

```text
d ~= 2D.
```

That is a concrete coordinate system for the surviving off-line-pair bridge problem. The next gate, if opened, should attack the smallest known multi-pair counterexample in these coordinates rather than search for another abstract invariant.
