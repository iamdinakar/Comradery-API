# Generated by Django 2.2.7 on 2020-02-15 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0047_auto_20200214_2158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='num_other_ats',
        ),
    ]