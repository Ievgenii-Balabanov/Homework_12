import requests
from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def add(x, y):
    return x + y


@shared_task
def send_email(subject, message, from_email):
    send_mail(subject, message, settings.NOREPLY_EMAIL, [from_email])
