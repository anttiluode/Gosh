# Gate 7 — Derivative channels do not escape a two-moment certificate

## Motivation

Gate 6 killed the safest scalar use of smoothed Laguerre information: after nonnegative squaring it becomes one ordinary bandwidth-one pair/form-factor certificate.

The natural objection is:

> do not square the transverse information into one scalar. Keep several signed/Hermitian channels — value, first derivative, second derivative, several apertures — and let the matrix structure preserve what `L2` knew.

This gate asks whether that can help **while the final certificate still uses only the two matrix quantities used by the 2026 rank–trace argument: trace and Hilbert–Schmidt/Frobenius norm squared.**

The answer is no, for a very general reason.

---

## 7A — matrix-valued translation-invariant kernels

Let each point `x_i` carry `c` analysis channels. The channels may be derivatives, different windows, different polynomial frequency weights, or any finite vector-valued feature map whose cross-Gram kernel is translation invariant:

```text
K(d) in C^(c x c),
K(-d)=K(d)^*.
```

Build the block Gram matrix

```text
G[(i,r),(j,s)] = K_rs(x_i-x_j).
```

Then two identities are immediate.

### Trace

Every diagonal point block is `K(0)`, so

```text
tr G = number_of_points * tr K(0)
```

(up to multiplicity weights if points are marked).

### Hilbert–Schmidt norm

```text
||G||_HS^2
 = sum_{i,j} sum_{r,s} |K_rs(x_i-x_j)|^2
 = sum_{i,j} ||K(x_i-x_j)||_F^2.
```

Thus both quantities depend only on the multiset of pair differences.

No choice of finitely many derivative channels changes that statement.

---

## 7B — the homometric attacker generalizes automatically

Gate 1 uses

```text
A={0,1,4,10,12,17}
B={0,1,8,11,13,17},
```

which have exactly the same multiset of pairwise differences.

Therefore for **every** matrix-valued translation-invariant kernel `K`,

```text
tr G_A = tr G_B,
||G_A||_HS^2 = ||G_B||_HS^2.
```

This is not a numerical property of sinc kernels. It is an exact information-theoretic no-go.

So if a derivative-augmented Clockfield/Laguerre construction is eventually compressed back to

```text
trace + Frobenius second moment + the usual block-count side information,
```

then the extra channels did not add a new kind of observable. They only changed the pair kernel.

---

## 7C — derivative jets preserve support but not correlation order

A concrete channel family makes the connection explicit. Let a compactly supported spectral window have weight `w(xi)` on `[-B,B]`, and define Fourier-side jet channels

```text
q_r(xi) = (2 pi i xi)^r sqrt(w(xi)),   r=0,...,R.
```

The cross-kernel is

```text
K_rs(d)
 = integral q_r(xi) conjugate(q_s(xi)) exp(2 pi i xi d) dxi.
```

Multiplying by powers of `xi` does not enlarge the Fourier support. So derivative jets are attractive analytically: they provide transverse/derivative information without paying extra support.

But at trace/HS order they remain pair data, because the preceding identities do not care what produced `K`.

This separates two notions that were easy to conflate:

```text
derivative order can grow without support growing,
correlation order does NOT grow until the matrix statistic grows beyond order two.
```

---

## 7D — the experiment

The branch builds the jet kernel above with a smooth compact spectral taper at bandwidth `.4`, using channel orders `R=0,1,2,3`.

For each order it forms the full block Gram matrix on the homometric pair and measures

```text
tr G,
||G||_F^2,
tr(G^3).
```

Results:

```text
R=0:  Δtr=0       Δ||G||²=0              Δtr(G³)=0.0000407
R=1:  Δtr=0       Δ||G||²=1.3e-15        Δtr(G³)=0.001014
R=2:  Δtr=0       Δ||G||²=2.7e-15        Δtr(G³)=0.067624
R=3:  Δtr=0       Δ||G||²=0              Δtr(G³)=0.064242
```

The first two moments tie exactly as predicted. The third moment escapes the tie because it assembles pair edges into closed triangles.

The numerical size of `Δtr(G^3)` is not important. Its nonzero value is only a sanity check for the structural distinction.

---

## 7E — what this says about the Laguerre/Clockfield escape

Keeping `L1,L2,...` as derivative channels is not useless. It can create a richer zero-side matrix and may expose local sign-indefinite structure.

But if the prime side supplies only

```text
tr G,
||G||_HS^2,
```

then any finite collection of translation-equivariant derivative windows is still visible only through pair data.

The 2026 rank–trace certificate cannot tell two homometric configurations apart from those inputs.

To exploit the richer channels, one must add at least one of:

1. a higher matrix moment such as `tr(G^3)` or `tr(G^4)`;
2. a non-translation-invariant/local center observable not reducible to pair differences;
3. an independent configuration-wise constraint on the zero-side blocks that is not encoded in trace/HS pair data;
4. a genuinely different prime-side arithmetic input.

Options 1 and 4 are precisely where higher prime correlations are expected to reappear. Option 2 loses the clean pair-correlation arithmetic. Option 3 is the only possible low-bandwidth loophole left in this architecture.

---

## Verdict

**Gate 7 is another clean negative, but a useful one.**

Derivative depth is not the same thing as correlation depth.

You can add arbitrarily many transverse/Laguerre jet channels without expanding Fourier support, but if you summarize the resulting Hermitian matrix only by its first two spectral moments, you have not escaped pair information. A homometric attacker defeats the entire finite channel family at once.

This gives `Gosh` a fairly hard boundary:

```text
more channels + same two moments  -> pair wall
higher matrix moment              -> arithmetic correlation wall
local non-pair constraint         -> only remaining low-support loophole
```

The next gate should therefore not add `L3` or another derivative channel. It should ask whether the **off-line hyperbolic block structure itself supplies a configuration-wise constraint beyond pair form factor that survives in a multi-channel matrix before taking higher moments.**