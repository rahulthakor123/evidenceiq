from truth_investigator.retrieval.tfidf_retriever import (
    TfidfRetriever,
)


class RetrievalPipeline:

    def __init__(self, documents: list[dict]):

        self.retriever = TfidfRetriever(
            documents
        )

    def search(
        self,
        claim: str,
        top_k: int = 5,
    ):

        return self.retriever.retrieve(
            claim,
            top_k=top_k,
        )