from pydantic import BaseModel, Field


class CurrencyResult(BaseModel):
    id: int = Field(gt=0)
    name: str = Field(min_length=1)
