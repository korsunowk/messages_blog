from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views import generic
from comment.models import Comment
from django.contrib.auth.mixins import LoginRequiredMixin


class CommentListView(generic.ListView):
    model = Comment
    template_name = 'blog.html'

    def get_queryset(self):
        queryset = super(CommentListView, self).get_queryset()
        return queryset


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

            new_comment = render_to_string('comment/one_comment.html',
                                           {'node': new_comment})
            return JsonResponse(dict(success=True,
                                     new_comment=new_comment))
        return JsonResponse(dict(success=False))
