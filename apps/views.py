from django.db.models import F
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.decorators import action
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.models import Category, Product
from apps.serializers import CategoryModelSerializer, ProductModelSerializer


class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.filter(parent__isnull=True)
    serializer_class = CategoryModelSerializer
    filter_backends = [DjangoFilterBackend]
    ordering_fields = '__all__'


class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    permission_classes = (AllowAny,)

    @action(methods=['GET'], detail=False)
    def counter(self, request, pk=None):
        if uuid := request.GET.get('id'):
            Product.objects.filter(id=uuid).update(views=F('views') + 1)
            return Response()
        return Response('Not Found', status=404)
