from __future__ import absolute_import, unicode_literals
from celery import shared_task

from .services import Client_CryptoCompare, Client


@shared_task
def send_api_request():
    pass