from django.db import models

class camera(models.Model):
    first_name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    Qulification=models.CharField(max_length=100)
    mobileno=models.CharField(max_length=25)
    adress=models.CharField(max_length=500)