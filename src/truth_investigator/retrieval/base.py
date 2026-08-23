from abc import ABC, abstractmethod

from truth_investigator.models.retrieval import RetrievalResult


class Retriever(ABC):

    @abstractmethod
    def retrieve(
        self,
        query: str,
        top_k: int = 5,
    ) -> list[RetrievalResult]:
        pass