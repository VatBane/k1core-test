from datetime import datetime

from pydantic import BaseModel, Field

from currency.models import Block


class Filter(BaseModel):
    currency: str | None = Field(default=None, min_length=1)
    provider: str | None = Field(default=None, min_length=1)


class BlockResult(BaseModel):
    id: int = Field(gt=0)
    currency: str = Field(min_length=1)
    provider: str = Field(min_length=1)
    block_number: int = Field()
    created_at: datetime = Field()
    stored_at: datetime = Field()

    @classmethod
    def from_django(cls, block: Block):
        return cls(id=block.id,
                   currency=block.currency.name,
                   provider=block.provider.name,
                   block_number=block.block_number,
                   created_at=block.created_at,
                   stored_at=block.stored_at)


class BlocksByFilterResult(BaseModel):
    result: list[BlockResult]
    total: int = Field(ge=0)
