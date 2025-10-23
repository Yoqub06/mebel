from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128, null=True, blank=True)
    img = models.ImageField(upload_to="ctg/")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        return super(Category, self).save(*args, **kwargs)



class Mebel(models.Model):
    price_types = {
        ("usd", "USD"),
        ("uzs", "UZS"),
        ("rub", "RUB"),
    }
    ctg = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=128)
    price = models.PositiveIntegerField(default=0)
    price_type = models.CharField(max_length=3, choices=price_types)
