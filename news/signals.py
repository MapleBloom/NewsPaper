from django.conf import settings
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.core.mail import send_mail, EmailMultiAlternatives
from .models import Post, PostCategory
from django.template.loader import render_to_string


# def send_notification(post, subscribers):
#     for u, c in subscribers.items():
#         html_content = render_to_string(
#             'news/new_post_message.html',
#             {
#                 'post': post,
#                 'link': f'{settings.SITE_URL}/posts/{post.id}',
#                 'user': u,
#                 'category': c,
#             }
#         )
#         msg = EmailMultiAlternatives(
#             subject=f"Fresh update at {c} publications of our great News Portal",
#             body='',
#             from_email=settings.DEFAULT_FROM_EMAIL,
#             to=[u.email],
#         )
#         msg.attach_alternative(html_content, "text/html")
#         msg.send()
#
#
# @receiver(m2m_changed, sender=PostCategory)
# def new_post_message(sender, instance, **kwargs):
#     if kwargs['action'] == 'post_add':
#         subscribers = []
#         for cat in instance.category.all():
#             subscribers += [(u, cat) for u in cat.userCategory.all()]
#         subscribers = dict([(k[0],
#             ', '.join([f"'{v[1]}'" for v in subscribers if k[0] == v[0]])) for k in subscribers])
#         send_notification(instance, subscribers)


