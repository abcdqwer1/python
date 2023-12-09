from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer


@api_view(["GET"])
def postlist(request):
    posts = [
        {"title": "1", "content": "111"},
        {"title": "2", "content": "222"},
        {"title": "3", "content": "333"},
    ]
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def a(request):
    posts = [
        {"title": "1", "content": "111"},
        {"title": "2", "content": "222"},
        {"title": "3", "content": "333"},
    ]
    serializer = posts
    return Response(serializer)


@api_view(["GET", "POST"])
def b(request):
    # 만약 요청이 GET이면
    if request.method == "GET":
        posts = [
            {"title": "GET!", "content": "GET!!"},
        ]
        serializer = posts
        return Response(serializer)
    # 만약 요청이 POST면
    elif request.method == "POST":
        posts = [
            {"title": "POST!", "content": "POST!!"},
        ]
        serializer = posts
        return Response(serializer)


@api_view(["POST"])
def create_post(request):
    # request.data는 사용자가 전송한 데이터입니다.
    serializer = PostSerializer(data=request.data)

    # 유효성 검사 수행
    if serializer.is_valid():
        # 여기서는 저장하는 로직을 생략하고 유효한 데이터라고 가정
        return Response({"message": "Post is valid", "data": serializer.validated_data})
    else:
        # 유효하지 않은 데이터의 경우 오류 메시지 반환
        return Response(serializer.errors, status=400)