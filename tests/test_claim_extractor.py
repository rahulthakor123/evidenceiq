from truth_investigator.extraction.claim_extractor import (
    extract_candidate_claims,
)


def test_extract_candidate_claims():

    sentences = [
        "Researchers conducted a study on 500 patients.",
        "Did the treatment work?",
        "The treatment reduced blood pressure by 15 percent.",
    ]

    claims = extract_candidate_claims(
        sentences,
        source_id="paper_001",
    )

    assert len(claims) == 2
    assert claims[0].source_id == "paper_001"