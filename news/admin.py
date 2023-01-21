from django.contrib import admin
from .models import Author, Category, UserCategory, Post, PostCategory, Comment


def rating_up(modeladmin, request, queryset): # request — инфо о запросе; queryset — объекты, выделенные галочками
    for q in queryset:
        q.like()
        if hasattr(q, 'user'):
            q.user.author.update_rating()
        elif hasattr(q, 'author'):
            q.author.update_rating()


def rating_down(modeladmin, request, queryset):
    for q in queryset:
        q.dislike()
        if hasattr(q, 'user'):
            q.user.author.update_rating()
        elif hasattr(q, 'author'):
            q.author.update_rating()


rating_up.short_description = 'rating + 1'
rating_down.short_description = 'rating - 1'


class AuthorAdmin(admin.ModelAdmin):
    list_display = (str, 'rating')         # [field.name for field in Author._meta.get_fields()]
    search_fields = ('post__title', 'post__text')


class UserCategoryAdmin(admin.ModelAdmin):
    list_filter = ('categorySubscribe__category', 'userSubscribe__username')


class PostAdmin(admin.ModelAdmin):
    list_display = ('get_title', 'getpost', 'preview', 'author', 'date_in', 'rating')
    list_filter = ('post', 'category__category')
    search_fields = ('author__userAuthor__first_name', 'author__userAuthor__last_name')
    actions = [rating_up, rating_down]


class PostCategoryAdmin(admin.ModelAdmin):
    list_filter = ('category__category', 'post__title')


class CommentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Comment._meta.get_fields()]
    list_filter = ('user', 'post')
    actions = [rating_up, rating_down]


admin.site.register(Author, AuthorAdmin)
admin.site.register(Category)
admin.site.register(UserCategory, UserCategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory, PostCategoryAdmin)
admin.site.register(Comment, CommentAdmin)
# admin.site.unregister(Product)    # to unregister model
