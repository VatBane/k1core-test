from typing import Annotated

from django.core.exceptions import ObjectDoesNotExist
from fastapi import APIRouter, Body, HTTPException
from fastapi.params import Query

from currency.models import Block, Currency
from currency.schemas.block import Filter, BlockResult

router = APIRouter(prefix='/block', tags=['Block'])


@router.post('/by_filters')
def search_blocks(filter: Annotated[Filter, Body()],
                  limit: Annotated[int, Query(gt=0)] = 20,
                  offset: Annotated[int, Query(ge=0)] = 0,
                  ):
    filters = ''
    if filter.currency:
        filters += f"AND c.name = '{filter.currency}'\n"
    if filter.provider:
        filters += f"AND pr.name = '{filter.provider}'\n"

    # TODO fix
    # WARNING
    # very dangerous to SQL injections
    query = f"""
    SELECT bl.id, c.name, pr.name, bl.block_number, bl.created_at, bl.stored_at
    FROM currency_block bl
    JOIN currency_currency c ON bl.currency_id = c.id
    JOIN currency_provider pr ON bl.provider_id = pr.id
    WHERE 1 = 1
    {filters}
    ORDER BY created_at DESC
    """
    blocks = Block.objects.raw(query)[offset:offset + limit]

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
