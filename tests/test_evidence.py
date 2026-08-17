import pytest
from pydantic import ValidationError

from truth_investigator.models.evidence import Evidence


def test_valid_evidence():
    evidence = Evidence(
        text="Earth is about 4.54 billion years old.",
        source_id="source_001",
    )

    assert evidence.source_id == "source_001"


def test_empty_evidence_is_invalid():
    with pytest.raises(ValidationError):
        Evidence(
            text="",
            source_id="source_001",
        )