from typing import Annotated

from django.core.exceptions import ObjectDoesNotExist
from fastapi import APIRouter, Body, HTTPException
from fastapi.params import Query

from currency.models import Block, Currency, Provider
from currency.schemas.block import Filter, BlockResult

router = APIRouter(prefix='/block', tags=['Block'])


@router.post('/by_filters')
def search_blocks(filter: Annotated[Filter, Body()],
                  limit: Annotated[int, Query(gt=0)] = 20,
                  offset: Annotated[int, Query(ge=0)] = 0,
                  ):
    blocks = Block.objects.all()
    if filter.currency:
        blocks = blocks.filter(currency=Currency.objects.get(name=filter.currency))
    if filter.provider:
        blocks = blocks.filter(provider=Provider.objects.get(name=filter.provider))

    blocks = blocks[offset:offset + limit]

    result = [BlockResult.from_django(block) for block in blocks]

    return result


@router.get('/')
def get_info_about_block(block_id: Annotated[int | None, Query(gt=0)] = None,
                         currency: Annotated[str | None, Query(min_length=1)] = None,
                         block_number: Annotated[int | None, Query()] = None):
    if not block_id and not (currency and block_number):
        raise HTTPException(status_code=422, detail="Block ID or currency name with number must be provided!")

    try:
        if block_id:
            block = Block.objects.get(id=block_id)
        else:
            block = Block.objects.get(currency=Currency.objects.get(name=currency), block_number=block_number)
    except ObjectDoesNotExist:
        raise HTTPException(status_code=404, detail="Object doesn't exist!")

    result = BlockResult.from_django(block)

    return result
