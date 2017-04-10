from django.conf.urls import url

from comment import views


app_name = 'comment'
urlpatterns = [
    url(r'^$', views.CommentListView.as_view(), name='blog'),
    url(r'^create/', views.CommentCreateView.as_view(), name='create_comment'),
    url(r'update/(?P<pk>\d+)/$', views.CommentUpdateView.as_view(), name='update_comment'),
    url(r'delete/(?P<pk>\d+)/$', views.CommentDeleteView.as_view(), name='delete_comment')
]
