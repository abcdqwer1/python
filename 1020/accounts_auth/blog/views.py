from .models import Post
from .serializers import PostSerializer, RegisterSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django.contrib.auth.models import User

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


userregister = RegisterView.as_view()

class PostListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        post_list = Post.objects.all()
        serializer = PostSerializer(post_list, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
postlist = PostListAPIView.as_view()


# 공식문서: https://www.django-rest-framework.org/api-guide/generic-views/
# https://www.django-rest-framework.org/api-guide/generic-views/#concrete-view-classes
# 이렇게 다양한 APIView를 지원하지만 Router를 사용하면 한 번에 