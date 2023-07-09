import time
from datetime import datetime, timedelta

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils import timezone

from academy.forms import ReminderForm


@shared_task
def add(x, y):
    return x + y


@shared_task
def send_email(from_email, message):
    send_email(from_email, message, ["noreply@hillel.io"])
