from django.db import models

from core.models import TimeStampModel

class Comment(TimeStampModel):
    content = models.CharField(max_length=1500)
    user    = models.ForeignKey('users.User', on_delete=models.CASCADE)
    post    = models.ForeignKey('posts.Post', on_delete=models.CASCADE)

    class Meta:
        db_table = 'comments'

    def __str__(self):
        return self.content
