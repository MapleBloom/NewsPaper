from modeltranslation.translator import register, TranslationOptions
from .models import Post, Comment


# @register(Post)
# class PostTranslationOptions(TranslationOptions):
#     fields = ('title', 'text')
#

@register(Comment)
class CommentTranslationOptions(TranslationOptions):
    fields = ('text', )
    empty_values = ''
