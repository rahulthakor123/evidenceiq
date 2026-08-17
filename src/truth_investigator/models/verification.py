from enum import Enum

from pydantic import BaseModel

from truth_investigator.models.evidence import Evidence


class Verdict(str, Enum):
    SUPPORTED = "supported"
    CONTRADICTED = "contradicted"
    MIXED = "mixed"
    INSUFFICIENT = "insufficient"


class VerificationResult(BaseModel):
    claim_id: str
    evidence: list[Evidence]
    verdict: Verdict
    confidence: float
    explanation: str