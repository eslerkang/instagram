from django.db   import models

from core.models import TimeStampModel

class Like(TimeStampModel):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE)

    class Meta:
        db_table='likes'
