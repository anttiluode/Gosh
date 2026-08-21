# Gate 4 status

**Question:** Is the second Laguerre layer arithmetically cheaper than a fourth Gram trace?

**Current answer:** algebraically yes, analytically not yet.

- Exact: `L2/f^2` is a pure two-zero interaction; the one-zero diagonal cancels.
- Obstruction: that normalized two-zero kernel has poles at the zeros, so it is not directly an admissible restricted-support n-level test.
- Regular `L2` is finite because the factor `f^2` cancels those poles, but then it is no longer a bare pair statistic.
- Next step: construct one entire bandlimited regularization and test whether its approximation error is small in a **certificate/inertia margin**, not merely in an L2 norm.

Toy follow-ups from Gate 2:

- with large legs fixed at `.70,.70`, `.05/.15` connectors beat `.10/.10`;
- on matched grids, doubling total aperture `1.6 -> 3.2` keeps the best two-small-leg absolute budget at `.20`, halving its fraction from `12.5%` to `6.25%`.

No improved zeta-zero proportion is claimed.