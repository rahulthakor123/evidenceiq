from pydantic import BaseModel, Field


class Evidence(BaseModel):
    evidence_id: str
    text: str = Field(min_length=1)
    source_id: str
    document_id: str
    score: float