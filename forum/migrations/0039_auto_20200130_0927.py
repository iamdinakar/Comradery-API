# Generated by Django 2.2.7 on 2020-01-30 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0038_auto_20200130_0859'),
    ]

    operations = [
        migrations.AddField(
            model_name='communityhost',
            name='primary',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='communityhost',
            name='community',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hosts', to='forum.Community'),
        ),
    ]