from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product

from .serializers import ProductSerializer

# Create your views here.
@api_view(['GET'])
def product_list(request):
    product = Product.objects.all() #сейчас в виде списка
    # print(product)
    # необходимо создать сериализатор, чтобы конвертировать в json
    serializer = ProductSerializer(product, many=True)
    return Response(serializer.data)
    