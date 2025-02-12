from typing import Annotated

from fastapi import APIRouter, Query

from currency.models import Currency

router = APIRouter(tags=['Currency'])


@router.get('/')
def get_list_currencies(limit: Annotated[int, Query(gt=0)] = 20,
                        offset: Annotated[int, Query(ge=0)] = 0,
                        ):
    currencies = Currency.objects.order_by('id')[offset:offset+limit]

    return currencies
