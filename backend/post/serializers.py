from rest_framework import serializers
from .models import Post

# Serializers is a way to convert Python data to API JSON format and vice-versa


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'