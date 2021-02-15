# Generated by Django 2.2.7 on 2020-02-14 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0045_auto_20200214_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='action_taker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.Person'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='notification_type',
            field=models.CharField(choices=[('CL', 'comment_like'), ('PL', 'post_like'), ('PC', 'post_comment'), ('CC', 'comment_comment')], max_length=5),
        ),
    ]
