from django.db import models

class User(models.Model):
    name = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    contact = models.CharField(max_length=50)
    mbti = models.CharField(max_length=4, blank=True)
    gender = models.CharField(max_length=9, choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('UNDEFINED', 'UNDEFINED')], default='UNDEFINED')

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.name
