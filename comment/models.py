from mptt.models import MPTTModel, TreeForeignKey
from django.db import models
from django.contrib.auth.models import User


class Comment(MPTTModel):
    user = models.ForeignKey(User)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    text = models.TextField('Comment', max_length=2*1024)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{0}: {1}".format(self.user.username, self.text)
