# Generated by Django 2.2.7 on 2020-03-21 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0067_auto_20200321_0812'),
    ]

    operations = [
        migrations.AddField(
            model_name='customfieldvalue',
            name='value',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
