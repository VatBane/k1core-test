from typing import Annotated

from fastapi import APIRouter, Query

from currency.routers.currency.controller import CurrencyRouterController


currency_router = APIRouter(prefix='/currency', tags=['Currency'])


@currency_router.get('/')
def get_list_currencies(limit: Annotated[int, Query(gt=0)] = 20,
                        offset: Annotated[int, Query(ge=0)] = 0,
                        ):
    controller = CurrencyRouterController()

    result = controller.get_currency_object(offset=offset, limit=limit)

    return result
