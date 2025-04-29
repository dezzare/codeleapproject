from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'username', 'title', 'content', 'created_datetime']
        read_only_fields = ['id', 'created_datetime']

    def update(self, instance, validate_data):
        if 'username' in validate_data:
            raise serializers.ValidationError({"username": "Not allowed to change this field"})
        return super().update(instance, validate_data)