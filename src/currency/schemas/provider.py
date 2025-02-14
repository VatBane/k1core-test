from pydantic import BaseModel, Field

from currency.models import Provider


class ProviderModel(BaseModel):
    id: int = Field(gt=0)
    name: str = Field(min_length=1)
    api_key: str = Field(min_length=1)

    @classmethod
    def from_django(cls, obj: Provider):
        return cls(id=obj.id,
                   name=obj.name,
                   api_key=obj.api_key)


class ProviderResult(BaseModel):
    result: list[ProviderModel]
    total: int = Field(ge=0)
