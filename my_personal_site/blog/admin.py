from django.contrib import admin

from .models import Author, Comment, Post, Tag
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('title', 'date', 'author', 'tags')
    list_display = ('title', 'date', 'author', 'slug')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('username', 'post', 'content')


admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
