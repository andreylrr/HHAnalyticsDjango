from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Regions(models.Model):
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    region = models.CharField(max_length=100)
    vac_city = models.CharField(max_length=50, default=" ")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.country + " " + self.region + " " + self.city


class Skills(models.Model):
    name = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Prof_Area(models.Model):
    name = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class Prof_Specs(models.Model):
    name = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class Vacancies(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=300)
    file_name = models.CharField(max_length=200)
    min_salary = models.FloatField()
    max_salary = models.FloatField()
    experience = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    region = models.ForeignKey(Regions, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skills)
    prof_spec = models.ManyToManyField(Prof_Specs)
    prof_area = models.ManyToManyField(Prof_Area)


    def __str__(self):
        return self.url

