from django.db   import models

from core.models import TimeStampModel

class Post(TimeStampModel):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    content = models.CharField(max_length=1500, blank=True)

    class Meta:
        db_table = 'posts'

    def __str__(self):
        return self.user.name+' - '+self.content


class Image(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    url = models.CharField(max_length=2048)

    class Meta:
        db_table = 'images'
