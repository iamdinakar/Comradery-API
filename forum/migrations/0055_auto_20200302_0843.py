# Generated by Django 2.2.7 on 2020-03-02 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0054_person_notification_frequency'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='welcome_content',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='community',
            name='welcome_title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
