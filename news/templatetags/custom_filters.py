from django import template
from django.template.defaultfilters import stringfilter
from better_profanity import profanity


register = template.Library()


LIKE_SYMBOLS = {
    'like': 'likes',
    'star': '*'
}
punctuation_list = ['.', ',', ';', ':', '...', '!', '?', '-', '"', '(', ')',
                    '@', '$', '*', '\n', '/']


@register.filter(name='likes_number')
def n_likes(value, code='like'):
    postfix = LIKE_SYMBOLS[code]
    return f'{value} {postfix}'


@register.filter()
def authorfullname(field):
    return f'{field.userAuthor.first_name} {field.userAuthor.last_name.upper()}'


@register.filter(name='censor')
@stringfilter
def cens(value, rcode='*'):
    str_v = value
    for x in punctuation_list:
        str_v = str_v.replace(x, ' ')
    str_v = str_v.split(' ')
    for v in str_v:
        if profanity.censor(v) != v:
            value = value.replace(v, f"{v[0]}{rcode * (len(v) - 1)}")
    return value
