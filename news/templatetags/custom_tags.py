from datetime import datetime
from django import template
from ..models import User

register = template.Library()


@register.simple_tag()
def current_time(format_string='%b %d %Y'):
    return datetime.utcnow().strftime(format_string)


@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    d = context['request'].GET.copy()
    for k, v in kwargs.items():
        d[k] = v
    return d.urlencode()


@register.simple_tag()
def user_deleter():
    for u in User.objects.all():
        if u.has_perm('news.delete_post') and u.id != 3:
            id_ = u.id
            break
    deleter = f'{User.objects.get(id=1).first_name} {User.objects.get(id=id_).last_name}'
    return deleter
