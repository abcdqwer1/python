from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Postblog
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthorOrReadOnly

class PostViewSet(ModelViewSet):
    queryset = Postblog.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

# 위 코드는 아래 코드와 같습니다.
# urls.py에서 url을 기본 제공하는 것만 사용해도 기본적으로 url도 분기해줍니다.
# def post_list(request):
#     # get
#     # post
#     pass

# def post_detail(request, pk):
#     # get
#     # put
#     # delete
#     pass



# 아래 코드는 저 기능중 단 1개만 사용합니다.
# class rest_framework import generics
# 
# class PostListAPIView(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
# post_list = PostListAPIView.as_view()


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