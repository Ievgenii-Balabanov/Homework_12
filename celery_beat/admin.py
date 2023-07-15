from django.contrib import admin

from celery_beat.models import Author, Quote

admin.site.register(Author)
admin.site.register(Quote)
