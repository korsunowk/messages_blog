from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect

from messages_blog import settings

import facebook
import json
from httplib2 import Http
import requests
import vk


class CallbackView(generic.View):

    @staticmethod
    def vk_callback(request):
        resp, content = Http().request(
            uri=settings.VK_URL + request.GET.get('code', ''),
            method='GET')

        content = json.loads(content.decode('ascii'))
        token = content['access_token']
        user_id = content['user_id']
        email = content['email']
        session = vk.Session(access_token=token)
        new_user_data = vk.API(session=session).users.get(user_ids=user_id)[0]
        username = "{0} {1}".format(new_user_data['first_name'], new_user_data['last_name'])

        if User.objects.filter(username=username).exists():
            new_user = User.objects.get(username=username)
        else:
            new_user = User.objects.create_user(
                username=username,
                email=email,
                password=user_id
            )

        auth.login(request, new_user)
        return redirect(reverse_lazy('comment:blog'))

    @staticmethod
    def facebook_callback(request):

        code = request.GET.get('code', False)
        resp, content = Http().request(
            uri=settings.FACEBOOK_URL.format(client_id=settings.FACEBOOK_APP,
                                             client_secret=settings.FACEBOOK_SECRET,
                                             code=code, domain=settings.DOMAIN),
            method='GET')

        content = json.loads(content.decode('ascii'))
        token = content['access_token']
        session = facebook.GraphAPI(access_token=token)
        args = {'fields': 'name,email'}
        new_user_data = session.get_object(id='me', **args)
        username = new_user_data['name']
        if User.objects.filter(username=username).exists():
            new_user = User.objects.get(username=username)
        else:
            new_user = User.objects.create_user(
                username=username,
                email=new_user_data['email'],
                password=new_user_data['id']
            )
        auth.login(request, new_user)
        return redirect(reverse_lazy('comment:blog'))

    @staticmethod
    def github_callback(request):
        code = request.GET.get('code', False)
        res = requests.post(settings.GITHUB_TOKEN_URL,
                            data={'client_id': settings.GITHUB_CLIENT,
                                  'client_secret': settings.GITHUB_SECRET,
                                  'code': code})
        content = res.content.decode('utf-8')

        token = content.split('&')[0].replace('access_token=', '')
        res = requests.get(settings.GITHUB_USER_URL,
                           {'access_token': token})
        content = res.json()

        if User.objects.filter(username=content['name']).exists():
            new_user = User.objects.get(username=content['name'])
        else:
            new_user = User.objects.create_user(
                username=content['name'],
                email=content['email'],
                password=content['id']
            )
        auth.login(request, new_user)
        return redirect(reverse_lazy('comment:blog'))
