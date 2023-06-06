from rest_framework.serializers import ModelSerializer


# add serializers
from rest_framework.serializers import ModelSerializer

from api_crud.models import Product, Category


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'



class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'short_description', 'image')


class ProductCreateSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'