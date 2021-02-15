# Generated by Django 2.2.7 on 2020-03-27 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0071_community_read_only'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommunityInvitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invite_code', models.CharField(max_length=40)),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.Community')),
            ],
        ),
    ]
