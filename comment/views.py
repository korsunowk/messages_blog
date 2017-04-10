from django.http import JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views import generic
from comment.models import Comment
from django.contrib.auth.mixins import LoginRequiredMixin


class CommentListView(generic.ListView):
    model = Comment
    template_name = 'blog.html'


class CommentCreateView(generic.CreateView, LoginRequiredMixin):
    model = Comment
    success_url = reverse_lazy('comment:blog')

    def post(self, request, *args, **kwargs):
        text = self.request.POST.get('text', None)
        user = self.request.user
        parent = self.request.POST.get('parent', None)

        if text:
            new_comment = Comment.objects.create(
                text=text,
                user=user,
                parent=parent if parent is None else Comment.objects.get(id=int(parent))
            )

            new_comment_str = render_to_string('comment/one_comment.html',
                                               {'node': new_comment,
                                                'new_child': parent,
                                                'user': self.request.user})

            return JsonResponse(dict(success=True,
                                     new_comment=new_comment_str,
                                     child=new_comment.id,
                                     parent=True if parent is None else False))

        return JsonResponse(dict(success=False))


class CommentUpdateView(generic.UpdateView, LoginRequiredMixin):
    model = Comment
    success_url = reverse_lazy('comment:blog')

    def post(self, request, *args, **kwargs):
        new_text = self.request.POST.get('text', None)
        comment = self.get_object()

        if new_text and self.request.user == comment.user:
            comment.text = new_text
            comment.save()
            return JsonResponse(dict(success=True, new_text=new_text))
        return JsonResponse(dict(success=False))


class CommentDeleteView(generic.DeleteView, LoginRequiredMixin):
    model = Comment
    success_url = reverse_lazy('comment:blog')

    def post(self, request, *args, **kwargs):
        comment = self.get_object()

        if self.request.user == comment.user:
            comment.delete()
            return JsonResponse(dict(success=True))
        return JsonResponse(dict(success=False))
