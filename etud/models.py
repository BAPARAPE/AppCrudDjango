from django.db import models

class User(models.Model):
    name = models.CharField(max_length=80)
    email = models.CharField(max_length=180)
    password = models.CharField(max_length=180)
