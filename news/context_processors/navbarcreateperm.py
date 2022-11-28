from datetime import datetime, timedelta
from ..models import *


def count_post_create(request, hours=24, limit=3):
    user = request.user
    today = datetime.now()
    count_period = today - timedelta(hours=hours)
    in_limit = 0
    if hasattr(user, 'author'):
        count_posts = Post.objects.filter(time_in__gte=count_period, author=user.author).count()
        in_limit = limit - count_posts if limit - count_posts > 0 else 0
    return {
        'in_limit': in_limit,
    }
