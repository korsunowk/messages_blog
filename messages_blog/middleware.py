from django.http import HttpResponsePermanentRedirect
from django.urls import reverse_lazy
from django.utils.deprecation import MiddlewareMixin


class Redirect404Middleware(MiddlewareMixin):
    def process_response(self, request, response):
        if response.status_code == 404:
            return HttpResponsePermanentRedirect(reverse_lazy('comment:blog'))

        return response
