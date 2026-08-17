from truth_investigator.models.claim import Claim
from truth_investigator.models.evidence import Evidence
from truth_investigator.models.source import Source
from truth_investigator.models.verification import (
    Verdict,
    VerificationResult,
)


def main():
    claim = Claim(
        text="The Earth is approximately 4.5 billion years old.",
        source_id="article_001",
    )

    evidence = Evidence(
        text="Scientists estimate the age of Earth to be about 4.54 billion years.",
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
        verdict=Verdict.SUPPORTED,
        confidence=0.95,
        explanation="The evidence directly supports the claim.",
    )

    print("CLAIM:")
    print(claim)

    print("\nEVIDENCE:")
    print(evidence)

    print("\nSOURCE:")
    print(source)

    print("\nVERIFICATION:")
    print(result)


if __name__ == "__main__":
    main()