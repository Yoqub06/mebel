import datetime
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

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=128)
    hex = models.CharField(max_length=6)

    def __str__(self):
        return self.name


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
    color = models.ManyToManyField(Color, related_name="colors")
    discount = models.SmallIntegerField(default=0)

    material = models.CharField(max_length=256, null=True)
    filled = models.CharField(max_length=128, null=True)

    g_length = models.PositiveIntegerField(default=233)
    g_width = models.PositiveIntegerField(default=107)
    g_height = models.PositiveIntegerField(default=90)

    is_spalniy = models.BooleanField(default=False)
    s_length = models.PositiveIntegerField(default=233, null=True, blank=True)
    s_width = models.PositiveIntegerField(default=0, null=True, blank=True)
    s_height = models.PositiveIntegerField(default=0, null=True, blank=True)

    extra = models.JSONField(default=dict)

    def __str__(self):
        return self.name

    def first_image(self):
        image = self.image.first()
        if image:
            return image.img.url
        else:
            return None

    def get_price(self):
        natija = int(self.price * (1 - self.discount / 100))
        return f"{natija:,}"

    def get_type(self):
        return self.price_type[self.price_type]


class MebelImage(models.Model):
    now = datetime.datetime.now().strftime("%Y/%m/%d/mebel/")
    img = models.ImageField(upload_to=str(now))
    mebel = models.ForeignKey(Mebel, on_delete=models.CASCADE, related_name="images")
