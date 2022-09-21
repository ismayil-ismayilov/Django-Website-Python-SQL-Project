from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
from django.db.models import DateTimeField
from django.db.models.functions import Trunc


class Country(models.Model):
    name = models.CharField(max_length=30)
    class Meta:
        db_table="country"

    def __str__(self):
        return str(self.name)


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    class Meta:
        db_table="city"

    def __str__(self):
        return str(self.name)


class Store(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    class Meta:
        db_table="store"

    def __str__(self):
        return str(self.name)


class Departments(models.Model):
    name = models.CharField(max_length=30)
    class Meta:
        db_table="departments"

    def __str__(self):
        return str(self.name)

class Ratings(models.Model):
    rating = models.CharField(max_length=30)
    class Meta:
        db_table="rating"

    def __str__(self):
        return str(self.rating)




class Review(models.Model):
    name = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE)
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    store = models.ForeignKey(Store, on_delete=models.SET_NULL, null=True)
    department = models.ForeignKey(Departments, on_delete=models.SET_NULL, null=True)
    rating = models.ForeignKey(Ratings, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.name)
