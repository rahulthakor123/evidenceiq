from truth_investigator.models.evidence import Evidence
from truth_investigator.retrieval.passage_retriever import (
    PassageRetriever,
)


class EvidencePipeline:

    def __init__(self, passages: list[dict]):

        self.retriever = PassageRetriever(
            passages
        )

    def retrieve(
        self,
        claim: str,
        top_k: int = 5,
    ) -> list[Evidence]:

        results = self.retriever.retrieve(
            claim,
            top_k=top_k,
        )

        evidence = []

        for index, result in enumerate(results):

            evidence.append(
                Evidence(
                    evidence_id=f"evidence_{index + 1}",
                    text=result["text"],
                    source_id=result["source_id"],
                    document_id=result["document_id"],
                    score=result["score"],
                )
            )

        return evidence