from pydantic import BaseModel, Field


class ProviderResult(BaseModel):
    id: int = Field(gt=0)
    name: str = Field(min_length=1)
    api_key: str = Field(min_length=1)
