import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class PassageRetriever:

    def __init__(self, passages: list[dict]):

        self.passages = passages

        self.vectorizer = TfidfVectorizer()

        self.matrix = self.vectorizer.fit_transform(
            [p["text"] for p in passages]
        )

    def retrieve(
        self,
        query: str,
        top_k: int = 5,
    ):

        query_vector = self.vectorizer.transform(
            [query]
        )

        scores = cosine_similarity(
            query_vector,
            self.matrix,
        )[0]

        indices = np.argsort(scores)[::-1][:top_k]

        results = []

        for index in indices:

            passage = self.passages[index].copy()

            passage["score"] = float(
                scores[index]
            )

            results.append(passage)

        return results