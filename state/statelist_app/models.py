from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=250)
    website = models.URLField(max_length=250)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Edification(models.Model):
    address = models.CharField(max_length=250)
    country = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    image = models.CharField(max_length=250)
    active = models.BooleanField(default=True)
    company=models.ForeignKey(Company, on_delete=models.CASCADE, related_name='edificacionlist')
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address

