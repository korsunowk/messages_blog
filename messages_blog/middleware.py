from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.deprecation import MiddlewareMixin


class Redirect404Middleware(MiddlewareMixin):
    def process_response(self, request, response):
        if response.status_code == 404:
            return redirect(reverse_lazy('comment:blog'))

        return response


class RedirectAuthUserFromLoginPage(MiddlewareMixin):
    def process_response(self, request, response):
        if request.user.is_authenticated() and request.path == reverse_lazy('login_page'):
            return redirect(reverse_lazy('comment:blog'))
        return response
