from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

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
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name='edificacionlist')
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address


class Comentary(models.Model):
    comentary_user = models.ForeignKey(User, on_delete=models.CASCADE)
    calification = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    text = models.CharField(max_length=200, null=True)
    edification = models.ForeignKey(
        Edification, on_delete=models.CASCADE, related_name='comentarios')
    active = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.calification)+' '+self.edification.address
