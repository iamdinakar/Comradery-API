# Generated by Django 2.2.7 on 2020-02-22 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0050_auto_20200222_0513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='digest_day_of_week',
            field=models.IntegerField(choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')], default=0),
        ),
    ]
