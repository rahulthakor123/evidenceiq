from pydantic import BaseModel


class Passage(BaseModel):
    passage_id: str
    document_id: str
    source_id: str
    text: str