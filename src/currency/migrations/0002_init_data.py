# Generated by Django 5.1.5 on 2025-02-13 22:52
from django.core.exceptions import ObjectDoesNotExist
from django.db import migrations


def init_currencies(apps, schema_editor):
    Currency = apps.get_model('currency', 'Currency')

    btc = Currency.objects.filter(name='Bitcoin').first()
    if not btc:
        # create BTC currency
        btc = Currency(name='Bitcoin')
        btc.save()

    eth = Currency.objects.filter(name='Ethereum').first()
    if not eth:
        # create ETH currency
        eth = Currency(name='Ethereum')
        eth.save()


def init_providers(apps, schema_editor):
    Provider = apps.get_model('currency', 'Provider')

    coin_market = Provider.objects.filter(name='CoinMarketCap').first()
    if not coin_market:
        # create CoinMarketCap provider
        coin_market = Provider(name='CoinMarketCap', api_key='NONE')
        coin_market.save()

    block_chair = Provider.objects.filter(name='BlockChair').first()
    if not block_chair:
        # create BlockChair provider
        block_chair = Provider(name='BlockChair', api_key='NONE')
        block_chair.save()


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(init_currencies),
        migrations.RunPython(init_providers),
    ]
