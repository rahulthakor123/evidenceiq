from pydantic import BaseModel


class RetrievalResult(BaseModel):
    document_id: str
    text: str
    score: float