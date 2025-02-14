import asyncio

from asgiref.sync import sync_to_async
from django.apps import AppConfig


class CurrencyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'currency'

    def ready(self):
        loop = asyncio.get_event_loop()

        if loop.is_running():
            asyncio.create_task(self.start_periodic_tasks())
        else:
            asyncio.run(self.start_periodic_tasks())

    async def start_periodic_tasks(self):
        from django_celery_beat.models import IntervalSchedule, PeriodicTask

        interval, _ = await sync_to_async(IntervalSchedule.objects.get_or_create)(
            every=60,
            period=IntervalSchedule.SECONDS,
        )

        await sync_to_async(PeriodicTask.objects.update_or_create)(
            interval=interval,
            name="load_btc",
            task="currency.tasks.load_btc",
        )

        await sync_to_async(PeriodicTask.objects.update_or_create)(
            interval=interval,
            name="load_eth",
            task="currency.tasks.load_eth",
        )

