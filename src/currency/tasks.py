from celery import shared_task


@shared_task
def load_data():
    print('Hello World!')
