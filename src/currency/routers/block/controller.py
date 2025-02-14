from django.core.exceptions import ObjectDoesNotExist

from currency.exceptions import ResourceNotFoundError
from currency.models import Block, Currency, Provider
from currency.schemas.block import BlockResult, BlocksByFilterResult, Filter


class BlockRouterController:
    def get_block_by_filters(self,
                             filters: Filter,
                             offset: int,
                             limit: int) -> BlocksByFilterResult:
        blocks = Block.objects.all()
        if filters.currency:
            blocks = blocks.filter(currency=Currency.objects.get(name=filters.currency))
        if filters.provider:
            blocks = blocks.filter(provider=Provider.objects.get(name=filters.provider))

        total = blocks.count()
        blocks = blocks[offset:offset + limit]

        result = [BlockResult.from_django(block) for block in blocks]

        return BlocksByFilterResult(result=result, total=total)

    def get_block_info(self,
                       block_id: int = None,
                       currency: str = None,
                       block_number: int = None,
                       ):
        try:
            if block_id:
                block = Block.objects.get(id=block_id)
            else:
                block = Block.objects.get(currency=Currency.objects.get(name=currency), block_number=block_number)
        except ObjectDoesNotExist:
            raise ResourceNotFoundError("Object doesn't exist!")

        result = BlockResult.from_django(block)
        return result
