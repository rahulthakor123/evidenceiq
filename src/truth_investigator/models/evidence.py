from pydantic import BaseModel, Field


class Evidence(BaseModel):
    text: str = Field(min_length=1)
    source_id: str