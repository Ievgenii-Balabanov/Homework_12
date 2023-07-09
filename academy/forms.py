from time import sleep

from django import forms
from django.core.exceptions import ValidationError
from django.core.mail import send_mail


class ReminderForm(forms.Form):
    from_email = forms.EmailField(required=True)
    message = forms.CharField(required=True)
    datetime = forms.DateTimeField(required=True)
