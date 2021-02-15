# Generated by Django 2.2.7 on 2020-02-25 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0052_channel_sort'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='community',
            name='ff_external_photo_enabled',
        ),
        migrations.RemoveField(
            model_name='post',
            name='should_reindex',
        ),
        migrations.AddField(
            model_name='notification',
            name='should_send_email',
            field=models.BooleanField(default=False),
        ),
    ]