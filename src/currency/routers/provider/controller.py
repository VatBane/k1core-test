from currency.models import Provider
from currency.schemas.provider import ProviderModel, ProviderResult


class ProviderRouterController:
    def get_all_providers(self,
                          limit: int,
                          offset: int,
                          ):
        providers = Provider.objects.all()
        total = providers.count()
        providers = providers[offset:offset + limit]

        result = [ProviderModel.from_django(provider) for provider in providers]

        return ProviderResult(result=result, total=total)
