from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Post
from .serializers import PostSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthorOrReadOnly

class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

post_list = PostListAPIView.as_view()

class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

post_detail = PostDetailAPIView.as_view()

class PostNewAPIView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

post_new = PostNewAPIView.as_view()


# 위 코드는 아래 코드와 같습니다.
# def post_list(request):
#     # get

# 아래 모든 코드가 위 코드(viewset) 3줄로 해결됨
# class BooksAPI(APIView):
#     def get(self, request):
#         books = Book.objecst.all()
#         serializer = BookeSerializer(books, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         serializer = BookeSerializer(books, many=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request):
#         books = Book.objects.all()
#         books.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class BookAPI(APIView):
#     def get(self, request, id):
#         book = get.object_or_404(Book, bid=id)
#         serializer = BookSerializer(book)
#         return Response(serializer.data, status=status.HTTP_200_OK)