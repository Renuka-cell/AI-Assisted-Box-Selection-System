from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id}"

class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items"
    )

    product = models.ForeignKey(
        "products.Product",
        on_delete=models.PROTECT,
        related_name="order_items"
    )

    quantity = models.PositiveIntegerField(
        validators=[MinValueValidator(1)]
    )

    def __str__(self):
        return f"{self.product.name} × {self.quantity}"