from datetime import datetime

from truth_investigator.models.claim import Claim
from truth_investigator.models.evidence import Evidence

from truth_investigator.models.verification import (
    Verdict,
    VerificationResult,
)

from truth_investigator.ingestion.text_loader import load_text_file
from truth_investigator.preprocessing.cleaner import clean_text
from truth_investigator.preprocessing.normalizer import normalize_text


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

def test_text_processing_pipeline():
    raw_text = load_text_file("data/raw/sample.txt")

    cleaned_text = clean_text(raw_text)

    normalized_text = normalize_text(cleaned_text)

    print("\n========== RAW TEXT ==========")
    print(raw_text)

    print("\n========== CLEANED TEXT ==========")
    print(cleaned_text)

    print("\n========== NORMALIZED TEXT ==========")
    print(normalized_text)

    assert "<p>" in raw_text
    assert "https://example.com" in raw_text
    assert "THE STUDY SHOWED" in raw_text

    assert "<p>" not in cleaned_text
    assert "https://example.com" not in cleaned_text

    assert "THE STUDY SHOWED" not in normalized_text
    assert "the study showed" in normalized_text

    assert (
        "researchers found that regular exercise improves cognitive performance."
        in normalized_text
    )

    