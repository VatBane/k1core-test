from datetime import datetime

from pydantic import BaseModel, Field


class BlockDTO(BaseModel):
    block_hash: str = Field(min_length=1, validation_alias="best_block_hash")
    block_height: int = Field(validation_alias="best_block_height")


class BlockDetailsDTO(BaseModel):
    block_number: int = Field(validation_alias='id')
    created_at: datetime = Field(validation_alias='time')
