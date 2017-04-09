from django.contrib import admin
from comment.models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ['get_creator_name', 'text', 'created']

    def get_creator_name(self, obj):
        return obj.user.username

    get_creator_name.short_description = 'Username'

admin.site.register(Comment, CommentAdmin)
