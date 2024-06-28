from django.db import models

# Create your models here.


class Property(models.Model):
    address = models.CharField(max_length=250)
    country = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    image = models.CharField(max_length=250)
    active = models.BooleanField(default=True)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address


class Company(models.Model):
    name = models.CharField(max_length=250)
    website = models.URLField(max_length=250)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
