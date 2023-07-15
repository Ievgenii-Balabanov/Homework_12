from django.db import models


class Author(models.Model):
    author = models.CharField(max_length=35)
    birth_date = models.CharField(max_length=70)
    hometown = models.CharField(max_length=30)
    description = models.CharField(max_length=500)


class Quote(models.Model):
    quote = models.CharField(max_length=300)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.author