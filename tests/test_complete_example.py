from datetime import datetime

from truth_investigator.models.claim import Claim
from truth_investigator.models.evidence import Evidence

from truth_investigator.models.verification import (
    Verdict,
    VerificationResult,
)


def test_complete_example():
    claim = Claim(
        claim_id="claim_001",
        text=(
            "Electric vehicles produce fewer lifetime greenhouse gas "
            "emissions than comparable gasoline vehicles."
        ),
        source_id="source_001",
        claim_type="fact",
        created_at=datetime.now(),
    )

    evidence_1 = Evidence(
        text=(
            "Electric vehicles generally produce fewer lifetime "
            "greenhouse gas emissions than gasoline vehicles."
        ),
        source_id="source_001",
    )

    evidence_2 = Evidence(
        text=(
            "Lifecycle analysis shows that electric vehicles "
            "typically have lower lifetime emissions."
        ),
        source_id="source_002",
    )

    evidence_3 = Evidence(
        text=(
            "The emissions advantage of electric vehicles increases "
            "when electricity comes from cleaner energy sources."
        ),
        source_id="source_003",
    )

    result = VerificationResult(
        claim_id=claim.claim_id,
        evidence=[
            evidence_1,
            evidence_2,
            evidence_3,
        ],
        verdict=Verdict.SUPPORTED,
        confidence=0.92,
        explanation=(
            "Multiple sources support the claim that electric vehicles "
            "generally produce fewer lifetime greenhouse gas emissions."
        ),
    )

    assert result.claim_id == claim.claim_id
    assert len(result.evidence) == 3
    assert result.verdict == Verdict.SUPPORTED
    assert result.confidence == 0.92