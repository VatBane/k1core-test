"""
ASGI config for django_app project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from fastapi import FastAPI

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_app.settings')

app = FastAPI()

application = get_asgi_application()


def init(app: FastAPI):
    from currency.routers.currency.router import router as currency_router
    from currency.routers.provider.router import router as provider_router
    from currency.routers.block.router import router as block_router

    app.include_router(currency_router)
    app.include_router(provider_router)
    app.include_router(block_router)

init(app)
