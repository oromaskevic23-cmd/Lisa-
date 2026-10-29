# Security Policy — LISA

**Current scope:** project identity, documentation, and an immutable presentation asset. No deployment or wallet signer is contained here.

## Reporting

Do not post secrets, wallet recovery phrases, private keys, credentials, sensitive customer data, or exploitable security details in public GitHub Issues. Where enabled, use GitHub private vulnerability reporting for this repository. Otherwise request a private disclosure route through the repository owner without including exploit details.

## Engineering boundaries

- Zero Trust and least privilege; fail closed on ambiguous authorization.
- AI Passport is identity, **not** permission or approval.
- Guardian Core, Approval Gateway, Owner Kill Switch and Audit Ledger are mandatory gates for any future agent-connected operation.
- No autonomous wallet signing, unrestricted transfers, trading manipulation, fake volume or unauthorized custody.
- Independent code review and contract security audits are distinct from ordinary GitHub Actions checks.
- All public claims about supply, fees, liquidity, exchange listings and ecosystem usage require independently verifiable dated evidence.

**No independent security audit is claimed by this repository.**
