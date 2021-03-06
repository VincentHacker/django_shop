from django.db import models
from django.contrib.auth import get_user_model
from slugify import slugify

# Create your models here.
'''
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self) -> str:
        return self.name
'''


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True) # то же что и CharField, только не разрешает использовать некоторые символы(есть проверки)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs) # можно просто super()

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(
                            Category, on_delete=models.CASCADE, related_name='product'
                            )
    image = models.ImageField(upload_to='product', blank=True, null=True)

    def __str__(self) -> str:
        return self.name


class Comment(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment from {self.author.name} to {self.product}'

    class Meta:
        verbose_name = 'Комментарий' #только в админке будет
        verbose_name_plural = 'Комментарии'
        ordering = ['-created_at'] # минус по убыванию