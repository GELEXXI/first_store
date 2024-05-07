from django.db import models
from users.models import User
from goods.models import Products


# Create your models here.
class CartQueryset(models.QuerySet):

    def total_price(self):
        return sum(cart.product_price() for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Cart(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        verbose_name="Користувач",
        blank=True,
        null=True,
    )
    product = models.ForeignKey(
        to=Products, on_delete=models.CASCADE, verbose_name="Товар"
    )
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name="Кількість")
    session_key = models.CharField(max_length=32, null=True, blank=True)
    create_timestamp = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата добавлення"
    )

    class Meta:
        db_table = "cart"
        verbose_name = "Кошик"
        verbose_name_plural = "Кошик"

    objects = CartQueryset().as_manager()

    def product_price(self):
        return round(self.product.sell_price() * self.quantity, 2)

    def __str__(self) -> str:
        return f"Корзина {self.user.username} | Товар {self.product.name} | Кількість {self.quantity}"
