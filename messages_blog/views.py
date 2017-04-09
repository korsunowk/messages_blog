from django.views import generic
from comment.models import Comment


class CommentListView(generic.ListView):
    model = Comment
    template_name = 'blog.html'
