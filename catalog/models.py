from django.db import models
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Category name')
    image_path = models.ImageField(upload_to=f'{__package__}/categories/', default=None, blank=True, null=True, verbose_name='Path to image')

    def __str__(self) -> str:
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=100, verbose_name='Country name')

    def __str__(self) -> str:
        return self.name

class State(models.Model):
    name = models.CharField(max_length=100, verbose_name='State, province or region name')

    def __str__(self) -> str:
        return self.name

class City(models.Model):
    name = models.CharField(max_length=100, verbose_name='City name')

    def __str__(self) -> str:
        return self.name

class Location(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, default=None, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True)

    def __str__(self) -> str:
        return self.city.name

class Item(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    pub_date = models.DateField(verbose_name='Publication date')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None, blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True)

    def __str__(self) -> str:
        return self.title
    

class Image(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    image_path = models.ImageField(upload_to=f'{__package__}/img/%Y%m%d/', blank=True, verbose_name='Path to image')
