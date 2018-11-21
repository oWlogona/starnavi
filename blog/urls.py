from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from blog.views import BlogList, BlogDetail, BlogLike

urlpatterns = format_suffix_patterns([
    path('blog/', BlogList.as_view()),
    path('blog/<int:pk>/', BlogDetail.as_view()),
    path('blog/<int:pk>/like/', BlogLike.as_view()),
])
