from typing import Annotated

from fastapi import APIRouter, Query

from currency.models import Provider
from currency.schemas.provider import ProviderResult

router = APIRouter(prefix='/provider', tags=['Provider'])


@router.get('/')
def get_list_providers(limit: Annotated[int, Query(gt=0)] = 20,
                       offset: Annotated[int, Query(ge=0)] = 0,
                       ):
    providers = Provider.objects.all()[offset:offset+limit]

    # dirty hack
    result = [ProviderResult(**provider.__dict__) for provider in providers]

    return result
