from truth_investigator.models.evidence import Evidence
from truth_investigator.models.verification import (
    Verdict,
    VerificationResult,
)


def test_supported_verdict():
    evidence = Evidence(
        text="Evidence supports the claim.",
        source_id="source_001",
    )

    result = VerificationResult(
        claim_id="claim_001",
        evidence=[evidence],
        verdict=Verdict.SUPPORTED,
        confidence=0.95,
        explanation="Evidence supports the claim.",
    )

    assert result.verdict == Verdict.SUPPORTED
    assert result.confidence == 0.95
    assert len(result.evidence) == 1