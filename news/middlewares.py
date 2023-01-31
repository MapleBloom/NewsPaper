import zoneinfo
from zoneinfo import ZoneInfoNotFoundError
from django.utils import timezone


class TimezoneMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            tzname = request.session.get('django_timezone')
            if tzname:
                timezone.activate(zoneinfo.ZoneInfo(tzname))
            else:
                timezone.deactivate()
        except ZoneInfoNotFoundError:
            tzname = 'UTC'
            timezone.activate(zoneinfo.ZoneInfo(tzname))
        except FileNotFoundError:
            tzname = 'UTC'
            timezone.activate(zoneinfo.ZoneInfo(tzname))
        return self.get_response(request)
