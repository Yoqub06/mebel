from .core import Mebel
from .auth import User

from django.db import models


class Cart(models.Model):
    mebel = models.ForeignKey(Mebel, on_delete=models.CASCADE, related_name='mcart')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart')
    quantity = models.PositiveIntegerField(default=0)
    total_price = models.PositiveIntegerField(default=0, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.total_price = self.mebel.price * self.quantity

