from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100) # то же что и CharField, только не разрешает использовать некоторые символы(есть проверки)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(
                            Category, on_delete=models.CASCADE, related_name='product'
                            )
    image = models.ImageField(upload_to='product')

    def __str__(self) -> str:
        return self.name


