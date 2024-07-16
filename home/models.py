from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    phone =models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Car(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    speed = models.IntegerField()

    def __str__(self):
        return self.name