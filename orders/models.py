from django.db import models

from django.contrib.auth import get_user_model

from product.models import Product


User = get_user_model()


STATUS_CHOICES = (
                ('open', 'Открыт'),
                ('in_process', 'В обработке'),
                ('cancelled', 'Отмененный'),
                ('finished', 'Завершенный')
                ) # choices нужен для того, чтобы ограничить возможность дополнительного заполнения (установили только 4)

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User,
                            on_delete=models.RESTRICT, related_name='orders'
                            )
    created_at = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=50, blank=True)
    products = models.ManyToManyField(Product, through='OrderItems')
    total_sum = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')

    def __str__(self):
        return f'Order #{self.id}'

class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.RESTRICT, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    quantity = models.PositiveSmallIntegerField(default=1)

'''
    def __str__(self) -> str:
        return f'Order #{self.id}' #если не указываем primary key, джанго по умолчанию создает id primary key

        '''