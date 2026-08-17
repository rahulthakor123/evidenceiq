from datetime import datetime
import pytest
from pydantic import ValidationError

from truth_investigator.models.claim import Claim


def test_valid_claim():
    claim = Claim(
        claim_id="claim_001",
        text="The Earth is approximately 4.5 billion years old.",
        source_id="article_001",
        claim_type="fact",
        created_at=datetime.now(),
    )

    assert claim.text
    assert claim.source_id == "article_001"


def test_empty_claim_is_invalid():
    with pytest.raises(ValidationError):
        Claim(
            claim_id="claim_001",
            text="",
            source_id="article_001",
            claim_type="fact",
            created_at=datetime.now(),
        )