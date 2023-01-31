from modeltranslation.translator import register, TranslationOptions
from django.contrib.flatpages.models import FlatPage
from .models import Post, Comment


@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


@register(Comment)
class CommentTranslationOptions(TranslationOptions):
    fields = ('text', )
    empty_values = ''


@register(FlatPage)
class FlatPageTranslationOptions(TranslationOptions):
    fields = ('title', 'content')
