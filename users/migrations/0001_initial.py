# Generated by Django 3.2.9 on 2021-11-25 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('contact', models.CharField(max_length=50)),
                ('mbti', models.CharField(blank=True, max_length=4)),
                ('gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('UNDEFINED', 'UNDEFINED')], default='UNDEFINED', max_length=9)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
