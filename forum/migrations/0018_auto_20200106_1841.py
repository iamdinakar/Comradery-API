# Generated by Django 2.2.7 on 2020-01-06 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0017_auto_20200106_0520'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='external_photo_url',
            field=models.URLField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='superadmin_api_only',
            field=models.BooleanField(default=False),
        ),
    ]