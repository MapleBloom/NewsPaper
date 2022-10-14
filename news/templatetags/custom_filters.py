from django import template
from better_profanity import profanity


class CensorError(Exception):
    pass


register = template.Library()

LIKE_SYMBOLS = {
    'like': 'likes',
    'star': 'stars'
}
punctuation_list = ['.', ',', ';', ':', '...', '!', '?', '-', '"', '(', ')',
                    '@', '$', '*', '\n', '/']

@register.filter(name='likes_number')
def n_likes(value, code='like'):
    postfix = LIKE_SYMBOLS[code]
    return f'{value} {postfix}'


@register.filter(name='censor')
def cens(value, rcode='*'):
    str_v = str(value)
    if not isinstance(str_v, str):
        raise CensorError('Only strings are subject to censor')

    for x in punctuation_list:
        str_v = str_v.replace(x, ' ')
    str_v = str_v.split(' ')
    for v in str_v:
        if profanity.censor(v) != v:
            value = value.replace(v, f"{v[0]}{rcode * (len(v) - 1)}")
    return value
