from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    years_of_experience = models.IntegerField()
    field_of_expertise = models.CharField(max_length=100)
    company = models.CharField(max_length=100)