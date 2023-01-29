# Generated by Django 4.1.2 on 2023-01-29 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_alter_post_category_alter_post_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='text_en_us',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='text_ru',
            field=models.TextField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(default=''),
        ),
    ]
