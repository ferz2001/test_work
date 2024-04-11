from django.db import models
from django.core.validators import MaxValueValidator


class Book(models.Model):
    name = models.CharField(max_length=20, null=False)
    title = models.CharField(max_length=30, blank=True)
    author = models.CharField(max_length=30, null=False)
    description = models.TextField(max_length=512, blank=True)
    price = models.IntegerField(validators=[MaxValueValidator(99999)])

    def __str__(self):
        return self.name


class Profile(models.Model):
    column_name = models.CharField(max_length=30, null=False, unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.column_name
