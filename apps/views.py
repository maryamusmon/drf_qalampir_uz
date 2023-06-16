from rest_framework.filters import SearchFilter
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from apps.models import Category, Blog
from apps.serializers import CategoryModelSerializer, BlogModelSerializer, SearchModelSerializer, SendEmailSerializer
from apps.tasks import send_message_email


class BlogModelViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogModelSerializer


class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


class BlogDetailRetrieveAPIView(RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogModelSerializer

    def retrieve(self, request, *args, **kwargs):
        self.get_queryset()
        instance = self.get_object()
        instance.view_count += 1
        instance.save()
        serializer = BlogModelSerializer(instance)
        return Response(serializer.data)


class SearchModelSearchAPIView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = SearchModelSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description']


class SendMailAPIView(APIView):
    def post(self, request):
        try:
            serializer = SendEmailSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            name = serializer.validated_data.get('name')
            email = serializer.validated_data.get('email')
            phone = serializer.validated_data.get('phone')
            message = serializer.validated_data.get('message')
            send_message_email.delay(email, message)
            return Response({'success': True, 'message': 'Email sent!'})
        except Exception as e:
            return Response({'success': False, 'message': str(e)})

