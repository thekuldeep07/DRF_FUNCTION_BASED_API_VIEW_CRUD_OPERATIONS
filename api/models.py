from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.name = models.CharField(max_length=100)
    rollNo = models.IntegerField()
    address = models.CharField(max_length=300)

