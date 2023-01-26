from modeltranslation.translator import register, TranslationOptions
from .models import Category, Post, Comment


# @register(Category)
# class CategoryTranslationOptions(TranslationOptions):
#     fields = ('category', )
#
#
# @register(Post)
# class PostTranslationOptions(TranslationOptions):
#     fields = ('post', 'time_in', 'title', 'text')
#
#
# @register(Comment)
# class CommentTranslationOptions(TranslationOptions):
#     fields = ('text', 'time_in')
