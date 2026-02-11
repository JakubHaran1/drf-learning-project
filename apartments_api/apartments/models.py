from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class ApartmentModel(models.Model):
    title = models.CharField(max_length=125)
    description = models.CharField(max_length=250)
    city = models.CharField(max_length=125)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    rooms = models.IntegerField()
    area = models.DecimalField(decimal_places=2, max_digits=10)
    build = models.DateField(auto_now=False, auto_now_add=False)
    published = models.DateField(auto_now_add=False)
    pets = models.BooleanField(default=False)
    user = models.ForeignKey(
        User,  on_delete=models.CASCADE, blank=True, null=True, related_name='apartments')

    def __str__(self):
        return self.title


# Create your models here.
