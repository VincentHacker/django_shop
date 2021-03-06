from rest_framework import serializers
from .models import Product, Comment


# class ProductSerializer(serializers.Serializer):
#     name = serializers.CharField()
#     description = serializers.CharField()
#     price = serializers.DecimalField(max_digits=10, decimal_places=2)
#     image = serializers.ImageField()

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['comments'] = CommentSerializer(instance.comments.all(), many=True).data
        return rep


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'image']


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.email') # отображает, чтобы email был в режиме чтения

    class Meta:
        model = Comment
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        # product = self.context.get('product')
        validated_data['author'] = user
        # validated_data['product'] = product
        return super().create(validated_data)

