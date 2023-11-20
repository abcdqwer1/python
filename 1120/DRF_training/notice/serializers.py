from rest_framework.serializers import ModelSerializer
from .models import Post
from django.contrib.auth import get_user_model

class PostSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = [
            'id',
            'author',
            'title',
            'content',
            'created_at',
            'updated_at',
        ]