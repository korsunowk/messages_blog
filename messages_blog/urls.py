"""messages_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import reverse_lazy
from django.views.generic import RedirectView, TemplateView


from messages_blog import settings, views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^accounts/', include('django.contrib.auth.urls')),
    url(r'', include('comment.urls')),

    url(r'login_page/', TemplateView.as_view(template_name='login_page.html'), name='login_page'),
    url(r'^vk_login/$', RedirectView.as_view(url=settings.VK_REDIRECT), name='vk_login'),
    url(r'^vk_callback/', views.CallbackView().vk_callback, name='vk_callback'),
    url(r'^facebook_callback/', views.CallbackView().facebook_callback, name='facebook_callback'),
    url(r'^facebook_login/', RedirectView.as_view(url=settings.FACEBOOK_REDIRECT),
        name='facebook_login'),
    url(r'^github_login/', RedirectView.as_view(url=settings.GITHUB_REDIRECT), name='github_login'),
    url(r'^github_callback/', views.CallbackView().github_callback, name='github_callback')
] + static(settings.STATIC_URL, document_root=settings.STATIC_URL)

handler404 = RedirectView.as_view(url=reverse_lazy('comment:blog'))
