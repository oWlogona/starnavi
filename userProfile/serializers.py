from rest_framework import serializers
from userProfile.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('user', 'age', 'sex')


class UserSerializer(serializers.Serializer):
    user = serializers.CharField(max_length=50)
    token = serializers.CharField(max_length=150)
