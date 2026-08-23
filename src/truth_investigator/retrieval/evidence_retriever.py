from truth_investigator.models.evidence import Evidence
from truth_investigator.retrieval.tfidf_retriever import (
    TfidfRetriever,
)


class EvidenceRetriever:

    def __init__(self, documents: list[dict]):

        self.documents = documents

        self.retriever = TfidfRetriever(
            documents
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
                    text=result.text,
                    source_id=result.document_id,
                    document_id=result.document_id,
                    score=result.score,
                )
            )

        return evidence