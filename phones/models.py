from django.db import models
from django.utils.text import slugify

class Phone(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=20, decimal_places=1)
    image = models.URLField(max_length=300)
    release_date = models.DateField()
    lte_exists = models.BooleanField(max_length=50)
    slug = models.SlugField(max_length=200)


