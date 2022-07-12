from django.contrib import admin
from .models import Category, Product, Comment
# Register your models here.

'''
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('name', 'description', 'price', 'image', 'category') # можно убрать list_display, тогда по умолчанию все выдаст

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    prepopulated_fields = {'slug': ('name', )}


# admin.site.register(Category)Category
# admin.site.register(Product)
admin.site.register(Comment)
'''

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Comment)
