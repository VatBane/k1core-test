from pydantic import BaseModel, Field

from currency.models import Currency


class CurrencyModel(BaseModel):
    id: int = Field(gt=0)
    name: str = Field(min_length=1)

    @classmethod
    def from_django(cls, obj: Currency):
        return cls(id=obj.id,
                   name=obj.name)


class CurrencyResult(BaseModel):
    result: list[CurrencyModel]
    total: int = Field(ge=0)
