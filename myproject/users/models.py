from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=140)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = models.CharField(max_length=500)