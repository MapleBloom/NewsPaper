# Generated by Django 4.1.2 on 2022-11-23 21:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categorySubscribe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.category')),
                ('userSubscribe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='userCategory',
            field=models.ManyToManyField(through='news.UserCategory', to=settings.AUTH_USER_MODEL),
        ),
    ]