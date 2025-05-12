from django.core.validators import MinLengthValidator
from django.db import models
from Fruitipedia_App.fruits.validators import only_letters_validator


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
class Fruit(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        validators=[MinLengthValidator(2), only_letters_validator]
    )
    image_url = models.URLField(max_length=500)
    description = models.TextField()
    nutrition = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_fruits', null=True, blank=True)