from django.http import JsonResponse
from django.views import generic
from comment.models import Comment
from django.contrib.auth.mixins import LoginRequiredMixin


class CommentListView(generic.ListView):
    model = Comment
    template_name = 'blog.html'


class CommentCreateView(generic.CreateView, LoginRequiredMixin):
    model = Comment
    success_url = '/'

    def post(self, request, *args, **kwargs):
        text = self.request.POST.get('text', None)
        user = self.request.user
        parent = self.request.POST.get('parent', None)
        if text:
            new_comment = Comment.objects.create(
                text=text,
                user=user,
                parent=parent
            )
            return JsonResponse(dict(success=True))
        return JsonResponse(dict(success=False))
