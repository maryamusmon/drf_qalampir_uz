from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.views import CategoryListCreateAPIView, ProductModelViewSet

routers = DefaultRouter()
routers.register('product_mixins', ProductModelViewSet, '')
urlpatterns =[
    path('', include(routers.urls)),
    path('category', CategoryListCreateAPIView.as_view(), name='category'),
    # path('product', ProductModelViewSet.as_view(), name='product')
]