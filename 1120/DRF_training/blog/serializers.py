from rest_framework.serializers import ModelSerializer
from .models import Postblog
from django.contrib.auth import get_user_model


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email']


class PostSerializer(ModelSerializer):
    author = AuthorSerializer()
    class Meta:
        model = Postblog
        fields = [
            'id',
            'author',
            'title',
            'content',
            'created_at',
            'updated_at',
        ]