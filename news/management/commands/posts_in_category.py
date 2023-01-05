from django.core.management.base import BaseCommand, CommandError
from news.models import Post, Category


def cat_list():
    cat_l = []
    for cat in Category.objects.all():
        cat_l.append(f'          {cat}')
    return '\n'.join(cat_l)


class Command(BaseCommand):
    help = 'print all posts in category'  # показывает подсказку при вводе "python manage.py <ваша команда> --help"

    missing_args_message = f'enter command with category name:\n{cat_list()}\n'

    requires_migrations_checks = True  # напоминать ли о том, что не сделаны все миграции (если такие есть)

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('category', type=str)

    def handle(self, *args, **options):
        try:
            category = [Category.objects.get(category=cat) for cat, hr in Category.CATEGORIES
                        if hr.lower() == options['category'].lower()][0]
            for pos in Post.objects.filter(category=category):
                self.stdout.write(str(pos))
        except IndexError or Category.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'There is no "{options["category"]}" category'))
