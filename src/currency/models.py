from django.db import models


# Create your models here.
class Currency(models.Model):
    id_: models.IntegerField(name="id", primary_key=True)
    name = models.CharField(max_length=16, unique=True)


class Provider(models.Model):
    id_: models.IntegerField(name="id", primary_key=True)
    name = models.CharField(max_length=64, unique=True)
    api_key = models.CharField(max_length=64)


class Block(models.Model):
    id_: models.IntegerField(name="id", primary_key=True)
    currency = models.ForeignKey(Currency, to_field='id', on_delete=models.CASCADE)
    provider = models.ForeignKey(Provider, to_field='id', on_delete=models.CASCADE)
    block_number = models.IntegerField()
    created_at = models.DateTimeField()
    stored_at = models.DateTimeField()
