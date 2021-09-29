from django.db import models

# Create your models here.


class Users(models.Model):
    name = models.CharField(max_length=30, null=False)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=9)
    age = models.IntegerField()
    birthday = models.DateField()
    married = models.BooleanField()







