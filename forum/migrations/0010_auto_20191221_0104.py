# Generated by Django 2.2.7 on 2019-12-21 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0009_auto_20191220_0059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='community',
        ),
        migrations.AddField(
            model_name='post',
            name='should_reindex',
            field=models.BooleanField(default=False),
        ),
    ]
