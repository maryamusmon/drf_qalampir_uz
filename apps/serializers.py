from rest_framework.serializers import ModelSerializer

# add serializers
from rest_framework.serializers import ModelSerializer

from apps.models import Category, Product


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

    def to_representation(self, instance):
        represent = super().to_representation(instance)
        data = CategoryModelSerializer(instance.children.all(), many=True).data
        represent['children'] = data if data else None
        return represent


class ProductModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
