from pydantic import BaseModel, HttpUrl


class Source(BaseModel):
    source_id: str
    title: str
    url: HttpUrl
    source_type: str