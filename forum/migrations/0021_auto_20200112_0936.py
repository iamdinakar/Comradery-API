# Generated by Django 2.2.7 on 2020-01-12 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0020_auto_20200108_0536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='name',
            field=models.CharField(max_length=12),
        ),
    ]
