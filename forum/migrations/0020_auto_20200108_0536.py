# Generated by Django 2.2.7 on 2020-01-08 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0019_auto_20200107_0757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='community',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='people', to='forum.Community'),
        ),
    ]
