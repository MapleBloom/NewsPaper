from django.contrib import admin
from .models import Author, Category, UserCategory, Post, PostCategory, Comment

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(UserCategory)
admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(Comment)
