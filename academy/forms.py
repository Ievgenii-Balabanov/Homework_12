import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone


class ReminderForm(forms.Form):
    from_email = forms.EmailField(required=True)
    message = forms.CharField(required=True)
    datetime = forms.DateTimeField(required=True)

    def clean_datetime(self):
        data = self.cleaned_data["datetime"]
        now = timezone.now()

        if data < now:
            raise ValidationError("Incorrect! Datetime can't be in the past!")

        if data > now + datetime.timedelta(days=2):
            raise ValidationError("Incorrect! The specified datetime is out of allowed range (2 days)!")
        return data
