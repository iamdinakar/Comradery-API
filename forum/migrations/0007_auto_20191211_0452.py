# Generated by Django 2.2.7 on 2019-12-11 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0006_auto_20191210_0645'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='upvotes',
            field=models.ManyToManyField(related_name='comment_upvoted', to='forum.Person'),
        ),
        migrations.AddField(
            model_name='post',
            name='score',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='upvotes',
            field=models.ManyToManyField(related_name='post_upvoted', to='forum.Person'),
        ),
    ]