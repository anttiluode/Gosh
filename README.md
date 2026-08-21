# Gosh

An intentionally silly name for a serious falsification workflow around Riemann-adjacent ideas.

> **This repository does not claim a proof of the Riemann Hypothesis.**
>
> The rule is the same as the better PerceptionLab repos: turn an intuition into a small mathematical gate, register what would kill it, and keep the negative result if it dies.

## Why this repo exists

The immediate prompt came from two otherwise unrelated lines:

1. **Claude / Alpöge–Furman (August 2026):** the new rank–trace / inertia argument proving that more than two thirds of zeta zeros are simple and on the critical line. The interesting structural move is to turn prime-side trace information into a constraint on how many negative directions the zero side can contain.
2. **AnttisBrain2 / HorizonNet (July 2026):** an apparently infinite hall of mirror moons became observationally complete after four bounces because one repeated operator contracted both amplitude and visible resolution. HorizonNet later clarified the important lesson: the useful horizon belongs in the *observer/decision*, not automatically in the internal state.

The question for `Gosh` is therefore not "can four terms solve an infinite zeta series?" They cannot. The question is:

> **Can an observation-horizon argument make an infinite operator / trace construction finite-to-certificate, without throwing away the arithmetic information that matters?**

That wording gives the idea somewhere precise to fail.

## Immediate stop line

The naive transplant is dead on arrival.

On the critical line, the ordinary Dirichlet / Euler expansions do not have a uniform contraction factor below one. In particular, prime amplitudes of size `p^(-1/2)` are not absolutely summable. So `4 = infinity` is **not** a valid truncation rule for zeta, the Euler product, or the prime orbit tower.

Analytic number theory already has sophisticated finite-horizon machinery — approximate functional equations, Riemann–Siegel type truncations, smoothed explicit formulas, compact Fourier support. Any useful result here must be stronger or differently targeted than simply rediscovering truncation.

## Branch map

```text
main
│
└── sol/gate0-moon-horizon
      Gate 0A  raw-series contraction test
      Gate 0B  Fredholm / Neumann zero-wall
      Gate 0C  certificate-space (spectral-margin) horizon
```

### `sol/gate0-moon-horizon` — current gate

Three claims are separated deliberately.

**0A — Raw series.** A fixed-depth moon-style horizon should fail for the critical-line Dirichlet / prime series. If it appears to work numerically without a rigorous tail bound, count that as a failure, not a discovery.

**0B — Operator horizon.** Suppose an analytic construction has

```text
D(s) = det(I - L_s)
```

with a trace-class operator `L_s`. If `||L_s|| < 1`, then Neumann / log-determinant tails can be bounded geometrically. But if `D(s)=0`, then `1` is an eigenvalue of `L_s`, so its spectral radius is at least one. Therefore a uniform contraction certificate cannot remain valid at the zero it is trying to detect. Registered prediction: the certified depth diverges as the model approaches the toy zero.

**0C — The surviving possibility: put the horizon in certificate space.** If a Hermitian object `G` is approximated by `G_K` and the uncomputed tail obeys

```text
||G - G_K||_op < delta,
```

then Weyl perturbation moves every eigenvalue by at most `delta`. Therefore, whenever the computed spectrum stays farther than `delta` from zero, the signs of those eigenvalues — hence the relevant inertia — are already certified. This is the direct analogue of AnttisBrain's "smaller than one pixel": the arithmetic tail need not literally vanish; it only has to become too small to change the final sign/inertia decision.

The reason this is potentially relevant to the 2026 rank–trace result is that its new information is explicitly **Hermitian/inertial**. The first experiment is only a toy. A later gate must use the actual finite Weil compression before any Riemann-facing claim is allowed.

## What would count as progress

- **Useful negative:** prove that any contraction horizon necessarily degenerates at the exact spectral points of interest. Keep the theorem and stop trying to use contraction as a proof engine.
- **Useful positive:** obtain a rigorous tail-to-inertia bound for an actual Weil-form compression, then show that a finite amount of arithmetic data certifies the same inertia statement as the untruncated object.
- **More interesting positive:** find a higher-trace / closed-walk certificate whose extra information survives a rigorous observation horizon and is not already contained in the bandwidth-one rank–trace framework.

Anything weaker — pretty zeta spirals, four-term coincidences, GUE-looking spectra, fits to known zeros — is not progress here.

## Related PerceptionLab repos

- `AnttisBrain2` — source of the four-bounce resolution-horizon observation.
- `HorizonNet` — the correction: a contraction certificate only recovers computation already below the decision resolution; the horizon belongs in the observer.
- `HilbertPolyaReintepretation` — prime loops / trace-log / delay-network formulation; useful language, but its Prime Orbit Condition + self-adjoint realizability lemma remains the cliff.
- `Alkuluku` — standing falsifier: generic RMT statistics are cheap; the arithmetic prime trace is the thing that must survive.
- `Nuoli` — broken time reversal can move a Hermitian construction from GOE toward GUE without making the spectrum complex; necessary symmetry mechanics, not the arithmetic solution.

## Ledger

**Known mathematics being reused:** Neumann series, Fredholm determinants, trace-log expansions, Banach contraction bounds, Weyl eigenvalue perturbation, Sylvester inertia, approximate functional equations / explicit-formula truncation.

**Current hypothesis:** an AnttisBrain-style *observation* horizon may be useful at the level of a Hermitian Riemann certificate even though it is useless as a fixed-depth truncation of zeta itself.

**Current status:** Gate 0 not yet run.

**Forbidden headline:** "four terms approximate the Riemann zeta function".

---

*Gosh is allowed to be a silly repo. Its controls are not allowed to be silly.*
