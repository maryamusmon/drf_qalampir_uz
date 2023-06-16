from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.views import CategoryModelViewSet, BlogModelViewSet, BlogDetailRetrieveAPIView, SearchModelSearchAPIView, \
    SendMailAPIView

routers = DefaultRouter()
routers.register('blog', BlogModelViewSet)
routers.register('category', CategoryModelViewSet)

urlpatterns = [
    path('', include(routers.urls)),
    path('blog_detail/<int:pk>', BlogDetailRetrieveAPIView.as_view()),
    path('search', SearchModelSearchAPIView.as_view()),
    path('send_email', SendMailAPIView.as_view()),
]