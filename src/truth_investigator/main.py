from datetime import datetime

from truth_investigator.ingestion.text_loader import load_text_file
from truth_investigator.preprocessing.cleaner import clean_text
from truth_investigator.preprocessing.normalizer import normalize_text

from truth_investigator.models.claim import Claim
from truth_investigator.models.evidence import Evidence
from truth_investigator.models.source import Source
from truth_investigator.models.verification import (
    Verdict,
    VerificationResult,
)


def process_text_file(file_path: str):
    raw_text = load_text_file(file_path)

    cleaned_text = clean_text(raw_text)

    normalized_text = normalize_text(cleaned_text)

    return raw_text, cleaned_text, normalized_text


def main():
    file_path = "data/raw/sample.txt"

    raw_text, cleaned_text, normalized_text = process_text_file(
        file_path
    )

    print("\n========== RAW TEXT ==========")
    print(raw_text)

    print("\n========== CLEANED TEXT ==========")
    print(cleaned_text)

    print("\n========== NORMALIZED TEXT ==========")
    print(normalized_text)

    claim = Claim(
        claim_id="claim_001",
        text="The Earth is approximately 4.5 billion years old.",
        source_id="article_001",
        claim_type="fact",
        created_at=datetime.now(),
    )

    evidence = Evidence(
        text=(
            "Scientists estimate the age of Earth to be "
            "about 4.54 billion years."
        ),
        source_id="usgs_001",
    )

    source = Source(
        source_id="usgs_001",
        title="Age of the Earth",
        url="https://example.com",
        source_type="government",
    )

    result = VerificationResult(
        claim_id="claim_001",
        evidence=[evidence],
        verdict=Verdict.SUPPORTED,
        confidence=0.95,
        explanation="The evidence directly supports the claim.",
    )

    print("\n========== CLAIM ==========")
    print(claim)

    print("\n========== EVIDENCE ==========")
    print(evidence)

    print("\n========== SOURCE ==========")
    print(source)

    print("\n========== VERIFICATION ==========")
    print(result)


if __name__ == "__main__":
    main()