# Generated by Django 2.2.7 on 2020-01-24 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0034_community_write_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='segment_user_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]