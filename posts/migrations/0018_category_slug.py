# Generated by Django 2.2 on 2020-03-17 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0017_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]
