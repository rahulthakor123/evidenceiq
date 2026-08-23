from truth_investigator.models.evidence import Evidence
from truth_investigator.models.verification import VerificationResult
from truth_investigator.verification.nli_verifier import NLIVerifier


class VerificationPipeline:

    def __init__(self, model_name: str):

        self.verifier = NLIVerifier(
            model_name
        )

    def verify(
        self,
        claim: str,
        evidence: list[Evidence],
    ) -> VerificationResult:

        return self.verifier.verify(
            claim,
            evidence,
        )