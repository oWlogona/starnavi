from django.contrib import admin
from blog.models import Blog, Like


class BlogAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Blog._meta.fields]


class LikeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Like._meta.fields]


admin.site.register(Blog, BlogAdmin)
admin.site.register(Like, LikeAdmin)
