# Generated by Django 2.2 on 2020-02-26 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20200225_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='overview',
            field=models.TextField(),
        ),
    ]
