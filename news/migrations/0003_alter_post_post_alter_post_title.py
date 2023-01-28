# Generated by Django 4.1.2 on 2023-01-28 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_usercategory_category_usercategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post',
            field=models.CharField(choices=[('N', 'News'), ('A', 'Article')], default='N', max_length=1, verbose_name='post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=128, verbose_name='title'),
        ),
    ]
