# Generated by Django 2.2.7 on 2020-01-16 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0024_auto_20200112_2259'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='ff_edit_profile_redirect_enabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='community',
            name='ff_external_photo_enabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='community',
            name='logout_redirect',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='edit_profile_redirect_url',
            field=models.URLField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='community',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='person',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
