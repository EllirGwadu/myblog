from django.contrib import admin
from .models import Post, Comments


class PostComments(admin.StackedInline):
    model = Comments
    extra = 1


class PostAdmin(admin.ModelAdmin):
    fields = ['author', 'title', 'text', 'created_date']
    inlines = [PostComments]


admin.site.register(Post, PostAdmin)
