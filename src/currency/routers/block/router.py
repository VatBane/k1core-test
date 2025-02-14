from typing import Annotated

from fastapi import APIRouter, Body, HTTPException
from fastapi.params import Query

from currency.exceptions import ResourceNotFoundError
from currency.routers.block.controller import BlockRouterController
from currency.schemas.block import Filter

block_router = APIRouter(prefix='/block', tags=['Block'])


@block_router.post('/by_filters')
def get_blocks_by_filters(filters: Annotated[Filter, Body()],
                          limit: Annotated[int, Query(gt=0)] = 20,
                          offset: Annotated[int, Query(ge=0)] = 0,
                          ):
    controller = BlockRouterController()

    result = controller.get_block_by_filters(filters=filters, limit=limit, offset=offset)
    return result


@block_router.get('/')
def get_block_info(block_id: Annotated[int | None, Query(gt=0)] = None,
                   currency: Annotated[str | None, Query(min_length=1)] = None,
                   block_number: Annotated[int | None, Query()] = None):
    if not block_id and not (currency and block_number):
        raise HTTPException(status_code=422, detail="Block ID or currency name with number must be provided!")

    controller = BlockRouterController()

    try:
        result = controller.get_block_info(block_id=block_id,
                                           currency=currency,
                                           block_number=block_number)
    except ResourceNotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc))

    return result
