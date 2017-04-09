from django.contrib import admin
from comment.models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ['text', 'created']


admin.site.register(Comment, CommentAdmin)
