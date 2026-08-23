import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from truth_investigator.models.retrieval import RetrievalResult
from truth_investigator.retrieval.base import Retriever


class TfidfRetriever(Retriever):

    def __init__(
        self,
        documents: list[dict],
    ):
        self.documents = documents

        self.vectorizer = TfidfVectorizer()

        self.matrix = self.vectorizer.fit_transform(
            [document["text"] for document in documents]
        )

    def retrieve(
        self,
        query: str,
        top_k: int = 5,
    ) -> list[RetrievalResult]:

        query_vector = self.vectorizer.transform([query])

        scores = cosine_similarity(
            query_vector,
            self.matrix,
        )[0]

        ranked_indices = np.argsort(scores)[::-1]

        results = []

        for index in ranked_indices[:top_k]:

            document = self.documents[index]

            results.append(
                RetrievalResult(
                    document_id=document["document_id"],
                    text=document["text"],
                    score=float(scores[index]),
                )
            )

        return results