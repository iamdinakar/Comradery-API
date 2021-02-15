# Generated by Django 2.2.7 on 2020-01-16 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0025_auto_20200116_0238'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=100)),
                ('label', models.CharField(max_length=15)),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to='forum.Community')),
            ],
        ),
    ]