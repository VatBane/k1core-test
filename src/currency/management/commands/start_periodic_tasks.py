import os
from django.core.management.base import BaseCommand
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from django.db import transaction


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Make sure the DJANGO_SETTINGS_MODULE is set
        if not os.environ.get('DJANGO_SETTINGS_MODULE'):
            self.stderr.write("DJANGO_SETTINGS_MODULE environment variable is not set!")
            return

        self.setup_periodic_tasks()
        self.stdout.write(self.style.SUCCESS('Successfully set up periodic tasks'))

    def setup_periodic_tasks(self):
        interval, _ = IntervalSchedule.objects.get_or_create(
            every=60,
            period=IntervalSchedule.SECONDS,
        )

        PeriodicTask.objects.update_or_create(
            interval=interval,
            name="load_btc",
            task="currency.tasks.load_btc",
        )

        PeriodicTask.objects.update_or_create(
            interval=interval,
            name="load_eth",
            task="currency.tasks.load_eth",
        )
