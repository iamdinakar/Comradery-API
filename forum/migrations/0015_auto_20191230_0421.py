# Generated by Django 2.2.7 on 2019-12-30 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0014_channel_emoji'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
