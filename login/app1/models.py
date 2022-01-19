from django.db import models

# Create your models here.
class employee(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)


