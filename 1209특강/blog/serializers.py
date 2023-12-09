from rest_framework import serializers

class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=10)
    content = serializers.CharField(max_length=100)
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['hello'] = 'hello world'
        return data