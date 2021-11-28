# Generated by Django 3.2.9 on 2021-11-28 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('likes', '0001_initial'),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='liked_user',
            field=models.ManyToManyField(related_name='liked_post', through='likes.Like', to='users.User'),
        ),
    ]