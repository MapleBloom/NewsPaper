from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from datetime import datetime
from django.urls import reverse
from django.core.cache import cache
from django.utils.translation import gettext as _
from django.utils.translation import gettext_lazy


class Author(models.Model):
    userAuthor = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.SmallIntegerField(default=0)

    def __str__(self):
        return f'{self.userAuthor.first_name} {self.userAuthor.last_name.upper()}'

    def update_rating(self):
        prt = self.post_set.aggregate(post_rating=Sum('rating'))
        post_rt = 0
        post_rt += prt.get('post_rating') if prt.get('post_rating') else 0

        crt = self.userAuthor.comment_set.aggregate(comment_rating=Sum('rating'))
        comment_rt = 0
        comment_rt += crt.get('comment_rating') if crt.get('comment_rating') else 0

        self.rating = post_rt * 3 + comment_rt
        self.save()


class Category(models.Model):
    CATEGORIES = [
        ('NW', gettext_lazy('News')),
        ('PL', gettext_lazy('Politics')),
        ('FN', gettext_lazy('Finance')),
        ('ED', gettext_lazy('Education')),
        ('AT', gettext_lazy('Auto')),
        ('SP', gettext_lazy('Sport')),
    ]

    category = models.CharField(max_length=2, choices=CATEGORIES, default='NW')
    userCategory = models.ManyToManyField(User, through='UserCategory')

    def __str__(self):
        return f'{self.get_category_display()}'


class UserCategory(models.Model):
    userSubscribe = models.ForeignKey(User, on_delete=models.CASCADE)
    categorySubscribe = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.userSubscribe} ~ {self.categorySubscribe}'


class Post(models.Model):
    POSTS = [
        ('N', gettext_lazy('News')),
        ('A', gettext_lazy('Article')),
    ]

    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    post = models.CharField(gettext_lazy('post'), max_length=1, choices=POSTS, default='N')
    time_in = models.DateTimeField(auto_now_add=True)
    title = models.CharField(gettext_lazy('title'), max_length=128)
    text = models.TextField(gettext_lazy('text'), default='In progress')
    rating = models.SmallIntegerField(default=0)

    category = models.ManyToManyField(Category, through='PostCategory', verbose_name=gettext_lazy('category'))

    def get_title(self):
        return str(self.title).upper()

    def __str__(self):
        return f'{self.get_title()}'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        cache.delete(f'post-{self.pk}')

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return f'{self.text[:50]}...'

    def getpost(self):
        return f'{self.get_post_display()}'

    def date_in(self):
        return self.time_in.date()


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.category.get_category_display()} ~ {self.post.get_title()}'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    text = models.TextField(default='...')
    time_in = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0)

    def __str__(self):
        return f'{self.text} of {self.user.first_name} {self.user.last_name.upper()} from '\
                  + f'{self.time_in.strftime("%d-%m-%y")} with rating {self.rating}'

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def date_in(self):
        return self.time_in.date()
