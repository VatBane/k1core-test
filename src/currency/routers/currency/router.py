from typing import Annotated

from fastapi import APIRouter, Query

from currency.models import Currency
from currency.schemas.currency import CurrencyResult

router = APIRouter(prefix='/currency', tags=['Currency'])


@router.get('/')
def get_list_currencies(limit: Annotated[int, Query(gt=0)] = 20,
                        offset: Annotated[int, Query(ge=0)] = 0,
                        ):
    currencies = Currency.objects.order_by('id')[offset:offset+limit]

    # dirty hack
    result = [CurrencyResult(**curr.__dict__) for curr in currencies]

    return result
