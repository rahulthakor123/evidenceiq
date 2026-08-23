from datetime import datetime

from truth_investigator.models.claim import Claim


def is_candidate_claim(sentence: str) -> bool:
    """
    Decide whether a sentence is a candidate claim.
    """

    sentence = sentence.strip()

    # Ignore empty sentences
    if not sentence:
        return False

    # Ignore questions
    if sentence.endswith("?"):
        return False

    # Ignore very short statements
    if len(sentence.split()) < 5:
        return False

    return True


def extract_candidate_claims(
    sentences: list[str],
    source_id: str,
) -> list[Claim]:

    claims = []

    for index, sentence in enumerate(sentences, start=1):

        if not is_candidate_claim(sentence):
            continue

        claim = Claim(
            claim_id=f"claim_{index:03d}",
            text=sentence,
            source_id=source_id,
            claim_type="candidate",
            created_at=datetime.utcnow(),
        )

        claims.append(claim)

    return claims