from transformers import pipeline

from truth_investigator.models.evidence import Evidence
from truth_investigator.models.verification import (
    Verdict,
    VerificationResult,
)
from truth_investigator.verification.base import Verifier


class NLIVerifier(Verifier):

    def __init__(
        self,
        model_name: str,
    ):
        self.classifier = pipeline(
            "text-classification",
            model=model_name,
        )

    def verify(
        self,
        claim: str,
        evidence: list[Evidence],
    ) -> VerificationResult:

        if not evidence:
            return VerificationResult(
                claim_id="unknown",
                verdict=Verdict.INSUFFICIENT,
                confidence=0.0,
                explanation="No evidence was retrieved.",
            )

        # First version:
        # evaluate the highest-ranked evidence.
        best_evidence = evidence[0]

        result = self.classifier(
            f"{best_evidence.text} [SEP] {claim}"
        )[0]

        label = result["label"]
        confidence = float(result["score"])

        if label.upper() == "ENTAILMENT":
            verdict = Verdict.SUPPORTED

        elif label.upper() == "CONTRADICTION":
            verdict = Verdict.CONTRADICTED

        else:
            verdict = Verdict.INSUFFICIENT

        return VerificationResult(
            claim_id="unknown",
            verdict=verdict,
            confidence=confidence,
            explanation=(
                f"NLI classified the evidence as {label}."
            ),
        )