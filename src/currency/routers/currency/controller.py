from currency.models import Currency
from currency.schemas.currency import CurrencyModel, CurrencyResult


class CurrencyRouterController:
    def get_currency_object(self,
                            offset: int,
                            limit: int,
                            ) -> CurrencyResult:
        currencies = Currency.objects.order_by('id')
        total = currencies.count()
        currencies = currencies[offset:offset + limit]

        # not the cleanest way :(
        result = [CurrencyModel.from_django(curr) for curr in currencies]

        return CurrencyResult(result=result, total=total)
