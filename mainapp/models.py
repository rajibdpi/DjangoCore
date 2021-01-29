from django.db import models

# Create your models here.


class Conatct(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=14)
    email = models.EmailField()
