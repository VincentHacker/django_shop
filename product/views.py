from venv import create #??
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView, CreateAPIView, 
    RetrieveAPIView, UpdateAPIView, DestroyAPIView,
    ListCreateAPIView, RetrieveUpdateDestroyAPIView) #done

from rest_framework.viewsets import ModelViewSet #done
from rest_framework.filters import SearchFilter #done
from rest_framework import permissions #done

from .models import Product, Comment #done
from .serializers import ProductSerializer, ProductListSerializer, CommentSerializer #done

from product.filter import ProductPriceFilter #done
from .permissions import IsAuthor #done


# Create your views here.
# закомментируем
'''
@api_view(['GET'])
def product_list(request):
    product = Product.objects.all() #сейчас в виде списка
    # print(product)
    # необходимо создать сериализатор, чтобы конвертировать в json
    serializer = ProductSerializer(product, many=True)
    return Response(serializer.data)
'''
# закомментируем
'''
class ProductsListView(APIView):
    def get(self, request):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)
'''

'''
class ProductsListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class CreateProductView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailsView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDeleteView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
'''
# можно объединить несколько классов (+ чтобы сократить urls при привязке url):
'''
class ProductRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
'''
#TODO: проверка прав (создавать, редактировать и удалять продукты могут только админы)
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # filterset_fields = ['category']
    filter_backends = [SearchFilter]
    search_fields = ['name', 'description']
    filterset_class = ProductPriceFilter
    permission_classes = [permissions.AllowAny]

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [permissions.AllowAny]
        elif self.action in ['destroy', 'update', 'partial_update', 'create']:
            self.permission_classes = [permissions.IsAdminUser]
        return super().get_permissions()


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action in ['destroy', 'update', 'partial_update']:
            self.permission_classes = [IsAuthor]
        return super().get_permissions()


'''
    @action(detail=True)
    def like(self):
        pass
'''


# post   -> 'create'
# get    -> 'list', 'retrieve'
# put    -> 'update'
# patch  -> 'partial_update'
# delete -> 'destroy'

    