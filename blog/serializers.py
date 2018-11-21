from rest_framework import serializers
from blog.models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('author', 'title', 'like_count', 'text', 'created_by')
