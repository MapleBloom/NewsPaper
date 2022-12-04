from datetime import datetime, timedelta
import logging
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from ...models import *

# logger = logging.getLogger(__name__)


# # наша задача
# def my_job():
#     today = datetime.now()
#     last_week = today - timedelta(days=7)
#     posts = Post.objects.filter(time_in__gte=last_week)
#     categories = set(posts.values_list('category__id', flat=True))
#     subscribers = set(User.objects.filter(category__in=categories))
#     for u in subscribers:
#         html_content = render_to_string(
#             'news/weekly_message.html',
#             {
#                 'posts': posts,
#                 'link': f'{settings.SITE_URL}',
#                 'user': u,
#             }
#         )
#         msg = EmailMultiAlternatives(
#             subject=f"Weekly publications update at our great News Portal",
#             body='',
#             from_email=settings.DEFAULT_FROM_EMAIL,
#             to=[u.email],
#         )
#         msg.attach_alternative(html_content, "text/html")
#         msg.send()
#
#
# def delete_old_job_executions(max_age=604_800):
#     """This job deletes all apscheduler job executions older than `max_age` from the database."""
#     DjangoJobExecution.objects.delete_old_job_executions(max_age)
#
#
# class Command(BaseCommand):
#     help = "Runs apscheduler."
#
#     def handle(self, *args, **options):
#         scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
#         scheduler.add_jobstore(DjangoJobStore(), "default")
#
#         # добавляем работу нашему задачнику
#         scheduler.add_job(
#             my_job,
#             trigger=CronTrigger(day_of_week="mon", hour="00", minute="00"), # second="*/25"),
#             # То же, что и интервал, но задача тригера таким образом более понятна django
#             id="my_job",  # уникальный айди
#             max_instances=1,
#             replace_existing=True,
#         )
#         logger.info("Added job 'my_job'.")
#
#         scheduler.add_job(
#             delete_old_job_executions,
#             trigger=CronTrigger(day_of_week="mon", hour="00", minute="20"),
#             # Каждую неделю будут удаляться старые задачи, которые либо не удалось выполнить, либо уже выполнять не надо.
#             id="delete_old_job_executions",
#             max_instances=1,
#             replace_existing=True,
#         )
#         logger.info(
#             "Added weekly job: 'delete_old_job_executions'."
#         )
#
#         try:
#             logger.info("Starting scheduler...")
#             scheduler.start()
#         except KeyboardInterrupt:
#             logger.info("Stopping scheduler...")
#             scheduler.shutdown()
#             logger.info("Scheduler shut down successfully!")
