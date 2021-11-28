from django.db   import models

from core.models import TimeStampModel

class User(TimeStampModel):
    id       = models.AutoField(primary_key=True)
    name     = models.CharField(max_length=15)
    email    = models.CharField(max_length=254, unique=True)
    password = models.CharField(max_length=200)
    contact  = models.CharField(max_length=19, unique=True)
    mbti     = models.CharField(max_length=4, blank=True)
    gender   = models.CharField(max_length=9)
    follow   = models.ManyToManyField(
        'self',
        symmetrical=False,
        through='Follow',
        through_fields=('follower', 'following')
    )

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.name


class Follow(TimeStampModel):
    follower  = models.ForeignKey('User', on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey('User', on_delete=models.CASCADE, related_name='following')
    is_bf     = models.BooleanField(default=False)

    class Meta:
        db_table = 'follows'
