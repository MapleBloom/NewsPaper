from datetime import datetime, timedelta
from django.utils import timezone
import zoneinfo
from ..models import Post


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


def sets_timezone(request):
    current_url = request.get_full_path()
    timezones = [x[:20] for x in zoneinfo.available_timezones()]
    timezones.sort()
    return {
        'current_date': timezone.localtime(timezone.now()).date,
        'current_time': timezone.localtime(timezone.now()).time,
        'current_utc': timezone.now().time,
        'current_hour': timezone.localtime(timezone.now()).hour,
        'timezones': timezones,
        'current_url': current_url,
    }
