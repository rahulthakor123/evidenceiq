from abc import ABC, abstractmethod

from truth_investigator.models.evidence import Evidence
from truth_investigator.models.verification import VerificationResult


class Verifier(ABC):

    @abstractmethod
    def verify(
        self,
        claim: str,
        evidence: list[Evidence],
    ) -> VerificationResult:
        pass