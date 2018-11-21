from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from userProfile.views import UserProfileList, UserSignIn, UserLogOut

urlpatterns = format_suffix_patterns([
    path('login/', UserSignIn.as_view(), name='user-login'),
    path('logout/', UserLogOut.as_view(), name='user-logout'),
    path('users/', UserProfileList.as_view(), name='user-list'),
])
