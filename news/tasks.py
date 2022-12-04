from celery import shared_task
import time
from datetime import datetime, timedelta
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .models import Post, User


@shared_task
def weekly_message():
    today = datetime.now()
    last_week = today - timedelta(days=7)
    posts = Post.objects.filter(time_in__gte=last_week)
    categories = set(posts.values_list('category__id', flat=True))
    subscribers = set(User.objects.filter(category__in=categories))
    for u in subscribers:
        html_content = render_to_string(
            'news/weekly_message.html',
            {
                'posts': posts,
                'link': f'{settings.SITE_URL}',
                'user': u,
            }
        )
        msg = EmailMultiAlternatives(
            subject=f"Weekly publications update at our great News Portal",
            body='',
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[u.email],
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()


def send_notification(post, subscribers):
    for u, c in subscribers.items():
        html_content = render_to_string(
            'news/new_post_message.html',
            {
                'post': post,
                'link': f'{settings.SITE_URL}/posts/{post.id}',
                'user': u,
                'category': c,
            }
        )
        msg = EmailMultiAlternatives(
            subject=f"Fresh update at {c} publications of our great News Portal",
            body='',
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[u.email],
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()


@shared_task
def new_post_message(pid):
    post = Post.objects.get(id=pid)
    subscribers = []
    for cat in post.category.all():
        subscribers += [(u, cat) for u in cat.userCategory.all()]
    subscribers = dict([(k[0],
        ', '.join([f"'{v[1]}'" for v in subscribers if k[0] == v[0]])) for k in subscribers])
    send_notification(post, subscribers)


@shared_task
def send_something():
    time.sleep(10)
    msg = EmailMultiAlternatives(
        subject=f"Weekly publications update at our great News Portal",
        body='blabla',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=['koyegiy813@ceoshub.com'],
    )
    msg.send()

# def hello():
#     time.sleep(10)
#     print("Hello, world!")
