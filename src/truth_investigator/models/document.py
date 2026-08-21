from datetime import datetime

from pydantic import BaseModel, Field


class Document(BaseModel):
    document_id: str
    title: str
    text: str = Field(min_length=1)
    source_id: str
    file_type: str
    created_at: datetime