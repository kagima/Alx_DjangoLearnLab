from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth import get_user_model

User = get_user_model()

# Post Serializer
class PostSerializer(serializers.ModelSerializer):
     author = serializers.StringRelatedField(read_only=True)  # Display the username, read-only
     
     class Meta:
         model = Post
         fields = ['id', 'author', 'title', 'content', 'created_at', 'updated_at']
         read_only_fields = ['id', 'author', 'created_at', 'updated_at']