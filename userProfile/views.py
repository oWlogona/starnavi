from rest_framework.views import APIView
from userProfile.models import UserProfile
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import authenticate
from rest_framework.permissions import IsAuthenticated
from userProfile.serializers import UserProfileSerializer, UserSerializer


class UserProfileList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, response, *args, **kwargs):
        user_list = UserProfile.objects.all()
        serilaizer = UserProfileSerializer(user_list, many=True)
        return Response(serilaizer.data)


class UserSignIn(APIView):

    def post(self, request, *args, **kwargs):
        user = authenticate(request, username=request.data.get('username'), password=request.data.get('password'))
        if user:
            token, created = Token.objects.get_or_create(user=user)
            content = {
                'user': user.username,
                'token': token.key,
            }
            serializer = UserSerializer(data=content)
            if serializer.is_valid():
                return Response(serializer.data)
            return Response(serializer.errors)
        return Response({'User': 'UNDEFINED'})


class UserLogOut(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        Token.objects.get(user=request.user).delete()
        return Response(status=204)
