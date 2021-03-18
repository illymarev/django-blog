from django.contrib import admin
from .models import Post, Comment

# Register your models here.

class CommentInline(admin.StackedInline):
    model = Comment
    readonly_fields = ['text', 'author']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [
        CommentInline
    ]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

