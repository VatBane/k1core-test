import datetime

from celery import shared_task

from currency.models import Block, Currency, Provider
from currency.services.block_chair.servicer import BlockChairAPIServicer


@shared_task
def load_btc():
    servicer = BlockChairAPIServicer()

    btc = Currency.objects.get(name='Bitcoin')
    block_chair = Provider.objects.get(name='BlockChair')
    block_dto = servicer.get_last_block(btc.name)
    block_details = servicer.get_block_details(btc.name, block_dto.block_hash)

    block = Block(currency_id=btc.id,
          provider_id=block_chair.id,
          block_number=block_details.block_number,
          created_at=block_details.created_at,
          stored_at=datetime.datetime.now()
          )
    block.save()


@shared_task
def load_eth():
    servicer = BlockChairAPIServicer()

    eth = Currency.objects.get(name='Ethereum')
    block_chair = Provider.objects.get(name='BlockChair')
    block_dto = servicer.get_last_block(eth.name)
    block_details = servicer.get_block_details(eth.name, block_dto.block_height)

    block = Block(currency_id=eth.id,
          provider_id=block_chair.id,
          block_number=block_details.block_number,
          created_at=block_details.created_at,
          stored_at=datetime.datetime.now()
          )
    block.save()