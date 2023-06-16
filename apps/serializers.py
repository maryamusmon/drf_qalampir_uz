from rest_framework.fields import CharField, EmailField

# add serializers
from rest_framework.serializers import ModelSerializer, Serializer

from apps.models import Category, Blog


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

    def to_representation(self, instance):
        represent = super().to_representation(instance)
        data = CategoryModelSerializer(instance.children.all(), many=True).data
        represent['children'] = data if data else None
        return represent


class BlogModelSerializer(ModelSerializer):
    class Meta:
        model = Blog
        exclude = ()


class SearchModelSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = ('title', 'description')


class SendEmailSerializer(Serializer):
    name = CharField(max_length=100)
    email = EmailField()
    phone = CharField(max_length=55)
    message = CharField(max_length=500)