# 가상환경은 미리 잡아주세요.

mkdir 1123
cd 1123

pip freeze > requirements.txt
# pip install -r requirements.txt # 추후 이 파일을 통해 설치합니다.

django-admin startproject project .
python manage.py migrate

# settings.py에서 접속할 수 있는 사람 설정
ALLOWED_HOSTS = ['*'] # 28번째 줄에 접속할 수 있는 사람을 모든 사람으로 변경

python manage.py startapp blog

# settings.py 에서 33번째 라인 수정
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
]

###################################
# tutorialdjango > urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
]

###################################
# blog > urls.py

from django.urls import path
from .views import MyAPIView

urlpatterns = [
    # ... 기존 URL 패턴들
    path('my-api-view/', MyAPIView.as_view(), name='my-api-view'),
]


###################################

pip install djangorestframework
pip install drf-spectacular

# pip install drf-yasg (swagger) ## 전에는 이거 많이 사용했습니다.

###################################

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # django lib app
    'rest_framework',
    'drf_spectacular',
    # custom app
    'blog',
]


REST_FRAMEWORK = {
    # YOUR SETTINGS  drf의 schema 클래스를 drf-specacular의 AutoSchema로 교체해줍니다.
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}


###################################
# project > urls.py

from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'), # API 스키마 제공(yaml파일)
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'), # 테스트할 수 있는 UI
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'), # API 문서화를 위한 UI
]

###################################


# blog > serializers.py

from rest_framework import serializers

class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    content = serializers.CharField(max_length=1000)

###################################

# blog > views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiParameter
from .serializers import PostSerializer

class MyAPIView(APIView):

    @extend_schema(
        request=PostSerializer,
        responses={200: PostSerializer}
    )
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            # 요청 데이터 처리
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
        
    @extend_schema(
        parameters=[
            OpenApiParameter(name='param', description='파라미터 설명', required=False, type=str)
        ],
        responses={200: {"description": "성공!!"},}
    )
    def get(self, request):
        param = request.query_params.get('param', None)
        return Response({"message": "GET 요청 처리됨", "param": param})

    # PUT, DELETE 등 다른 메서드에 대해서도 유사하게 적용 가능

###################################

# http://127.0.0.1:8000/blog/my-api-view/

{
    "title": "hello!",
    "content": "world!"
}


# http://127.0.0.1:8000/api/schema/swagger-ui/


{
    "title": "hello!",
    "content": "world!"
}
