from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from datetime import datetime
from django.urls import reverse


class Author(models.Model):
    userAuthor = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.SmallIntegerField(default=0)

    def __str__(self):
        return f'{self.userAuthor.first_name} {self.userAuthor.last_name.upper()}'

    def update_rating(self):
        prt = self.post_set.aggregate(post_rating=Sum('rating'))
        post_rt = 0
        post_rt += prt.get('post_rating')

        crt = self.userAuthor.comment_set.aggregate(comment_rating=Sum('rating'))
        comment_rt = 0
        comment_rt += crt.get('comment_rating')

        self.rating = post_rt * 3 + comment_rt
        self.save()


class Category(models.Model):
    CATEGORIES = [
        ('NW', 'News'),
        ('PL', 'Politics'),
        ('FN', 'Finance'),
        ('ED', 'Education'),
        ('AT', 'Auto'),
        ('SP', 'Sport'),
    ]

    category = models.CharField(max_length=2, choices=CATEGORIES, default='NW')

    def __str__(self):
        return f'{self.get_category_display()}'


class Post(models.Model):
    POSTS = [
        ('N', 'News'),
        ('A', 'Article'),
    ]

    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    post = models.CharField(max_length=1, choices=POSTS, default='N')
    time_in = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=128)
    text = models.TextField(default='In progress')
    rating = models.SmallIntegerField(default=0)

    category = models.ManyToManyField(Category, through='PostCategory')

    def get_title(self):
        return str(self.title).upper()

    def __str__(self):
        return f'{self.get_title()}'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return f'{self.text[:124]}...'

    def getpost(self):
        return f'{self.get_post_display()}'


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
