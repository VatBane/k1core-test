from typing import Annotated

from fastapi import APIRouter, Query

from currency.routers.provider.controller import ProviderRouterController

provider_router = APIRouter(prefix='/provider', tags=['Provider'])


@provider_router.get('/')
def get_list_providers(limit: Annotated[int, Query(gt=0)] = 20,
                       offset: Annotated[int, Query(ge=0)] = 0,
                       ):
    controller = ProviderRouterController()

    result = controller.get_all_providers(limit=limit, offset=offset)

    return result
