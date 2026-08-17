from pydantic import BaseModel, Field
from datetime import datetime


class Claim(BaseModel):
    claim_id: str
    text: str = Field(min_length=1)
    source_id: str
    claim_type: str
    created_at: datetime