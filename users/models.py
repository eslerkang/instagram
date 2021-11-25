from django.db   import models

from core.models import TimeStampModel

class User(TimeStampModel):
    name     = models.CharField(max_length=15)
    email    = models.CharField(max_length=254, unique=True)
    password = models.CharField(max_length=200)
    contact  = models.CharField(max_length=19, unique=True)
    mbti     = models.CharField(max_length=4, blank=True)
    gender   = models.CharField(max_length=9)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.name
