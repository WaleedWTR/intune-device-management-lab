# Windows Compliance Baseline

## Objective

Define a minimum endpoint posture that is understandable, measurable and operationally supportable.

## Example controls

- BitLocker enabled
- Secure Boot enabled
- host firewall enabled
- anti-malware enabled
- supported Windows version
- device remains actively managed
- exceptions are recorded and reviewed

## Deployment pattern

1. build the policy
2. validate in a test tenant
3. deploy to a small pilot ring
4. observe user and application impact
5. remediate known incompatibilities
6. expand gradually
7. measure compliance and exceptions
8. review baseline periodically

## Important

Compliance should not be treated as a binary dashboard alone. Investigate why devices fail and distinguish technical debt, stale devices, provisioning issues and genuine security risk.
