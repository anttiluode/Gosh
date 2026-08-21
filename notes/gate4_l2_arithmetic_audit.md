# Gate 4 — Is L2 really cheaper than a fourth trace?

## Question

Claude proposed that the first genuinely new Laguerre layer may be arithmetically cheaper than `tr(G^4)`.

The claim to audit is:

> `L2` is quartic in derivatives, but after passing to logarithmic derivatives its zero-side content contains only one-zero and two-zero pieces, so perhaps restricted-support 2-level correlation is enough.

This gate separates the algebraic statement from the analytic-number-theory statement.

## 4A — exact algebra: the diagonal cancels

Let `f` be an order-one real entire function with no Gaussian factor in its canonical product; this includes the Riemann Xi function. Write `g=log f` away from zeros.

The transverse expansion is

```text
|f(t+i y)|^2 = f(t)^2 + L1(t) y^2 + L2(t) y^4 + ...
```

with

```text
L1 = f'^2 - f f'',
L2 = f f''''/12 - f' f'''/3 + f''^2/4.
```

Using the logarithm,

```text
L2/f^2 = 1/2 (g'')^2 + 1/12 g''''.
```

For an order-one canonical product with zeros `z_j`,

```text
g''    = - sum_j 1/(t-z_j)^2,
g''''  = -6 sum_j 1/(t-z_j)^4.
```

Therefore

```text
L2/f^2
 = 1/2 (sum_j q_j)^2 - 1/2 sum_j q_j^2
 = sum_{j<k} q_j q_k,
q_j = 1/(t-z_j)^2.
```

So the one-zero diagonal cancels exactly:

> **the normalized second Laguerre layer is a pure two-zero interaction.**

This part of Claude's bookkeeping is correct.

## 4B — the catch: the clean two-zero statistic is singular

The arithmetic-friendly expression is not `L2`; it is `L2/f^2`.

Near a simple zero `z_j`,

```text
L2/f^2 ~ [sum_{k != j} 1/(z_j-z_k)^2] / (t-z_j)^2,
```

while `L2` itself stays finite because `f(t)^2 ~ f'(z_j)^2 (t-z_j)^2` cancels the pole.

The experiment in this branch verifies the scaling explicitly on a polynomial with four real zeros.

This matters because the classical restricted-support n-level theorems use admissible localized/entire test functions. The exact rational pair kernel above has poles at the zeros; it is not directly such a test.

So the slogan

```text
L2 = two-level -> Rudnick-Sarnak -> done
```

is not valid.

The cost has moved from **correlation order** to **regularization and certificate stability**.

## 4C — what a legitimate two-level route would need

A viable version would replace the singular kernel by an entire bandlimited surrogate. Schematically:

```text
q_j(t) = 1/(t-z_j)^2
        |
        v
bandlimited entire q_{j,B}(t)
        |
        v
sum_{j<k} q_{j,B}(t) q_{k,B}(t)
```

Then the zero-side object is genuinely pair-level and its Fourier support can be accounted for. But two new obligations appear:

1. **Arithmetic admissibility:** the regularized pair test must lie inside a range covered by an unconditional restricted-support theorem.
2. **Certificate stability:** replacing the exact Laguerre quantity by the bandlimited surrogate must preserve a configuration-wise inequality strong enough to say something about on-line/off-line blocks or inertia.

The second obligation is the more important one. A small approximation error in a statistic is not automatically a small error in a sign/inertia certificate — Gate 0 already taught us that the right comparison is against a decision margin.

## 4D — relation to the 2026 bandwidth-one ceiling

Alpöge–Furman explicitly describe a ceiling for certificates using only first/two-moment bandwidth-one information. Their paper also states that higher Gram moments become arithmetically expensive, with the diagonal method available in the Rudnick–Sarnak range `X^k <= T^(2-eps)`.

A bandlimited `L2` surrogate is attractive precisely because its zero-side combinatorics are only pair-level. But that creates a second possible death:

> it may be arithmetically cheaper **because it contains no information outside the pair-information class that already has the ~0.6818 bandwidth-one ceiling.**

This has not been proved here. To invoke the ceiling we would have to show that the chosen regularized `L2` functional is representable inside the exact information class used by the PairCeiling theorem.

So Gate 4 does not yet say `L2` improves the 67.25% theorem. It says the right next theorem-check is much narrower:

```text
Can a bandlimited entire regularization of L2/f^2
be written as an admissible pair statistic
that is NOT already redundant with the bandwidth-one Gram data?
```

## 4E — Gate 2 connector follow-ups

Claude proposed two cheap tests after its extreme edge-loading conjecture died.

### Fixed large legs: unequal small legs are genuinely better

```text
(.70,.05,.70,.15) -> 2.1541721037
(.70,.10,.70,.10) -> 1.9912477144
```

So the `.05/.15` split is not merely notation or a tie hidden by the old grid.

### Double the total budget on a matched scaled grid

Original search:

```text
total=1.6, step=.05, max leg=1.0
best (.70,.05,.70,.15)
small-leg sum = .20 = 12.5% of total
```

Scaled search:

```text
total=3.2, step=.10, max leg=2.0
best (1.40,.10,1.60,.10)
small-leg sum = .20 = 6.25% of total
```

On this toy and this matched discretization the connector budget stays approximately **absolute**, not proportional. This is not a universal law; it most likely reflects the fixed geometric scales of the homometric attacker and sinc kernel.

It also warns against over-interpreting the old `(0.70,0.05,0.70,0.15)` proportions as architecture-independent.

## Verdict

Claude's Gate 4 conjecture survives its first audit in a weaker but more interesting form.

**Verified:**

- `L2/f^2` is exactly a pure two-zero interaction; the one-zero diagonal cancels.
- the normalized object has second-order poles at simple zeros; the regular `L2` does not.
- unequal connector legs matter in the Gate 2 toy.
- doubling the toy support budget does not preserve the small-leg fraction on a matched grid.

**Not verified:**

- that an admissible bandlimited `L2` regularization gives new information beyond bandwidth-one pair data;
- that it maps to the Alpöge–Furman positive-index/inertia certificate;
- that it improves any zero proportion.

## Next gate

Do not jump to more moments yet.

Construct one explicit entire bandlimited approximation to the normalized pair kernel, then answer three yes/no questions:

1. what is its exact two-zero Fourier-support region?
2. is its averaged value covered unconditionally by the non-RH restricted-support correlation theorem?
3. can its approximation error be bounded against an inertia/sign margin, rather than merely in an L2 norm?

If (3) fails, the observation-horizon analogy has located its wall again.