from collections import OrderedDict
from datetime import datetime
from urllib.parse import urlencode, urlunparse

import requests
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils import timezone
from social_core.exceptions import AuthException, AuthForbidden

from authapp.models import UserProfile


def save_user_profile(backend, user, response, *args, **kwargs):
    if backend.name != 'vk-oauth2':
        return

    api_url = urlunparse(('http', 'api.vk.com', 'method/users.get', None,
                          urlencode(OrderedDict(fields=','.join(('bdate', 'sex', 'about', 'photo_200', 'personal')),
                                                access_token=response['access_token'], v=5.131
                                                )), None))
    resp = requests.get(api_url)
    if resp.status_code != 200:
        return
    data = resp.json()['response'][0]
    a = 0

    if data['sex'] == 1:
        user.userprofile.gender = UserProfile.FEEMALE
    elif data['sex'] == 2:
        user.userprofile.gender = UserProfile.MALE
    else:
        pass

    if data['about']:
        user.userprofile.about = data['about']

    bdate = datetime.strptime(data['bdate'], '%d.%m.%Y').date()
    age = timezone.now().date().year - bdate.year
    user.age = age
    user.first_name = data['first_name']
    user.last_name = data['last_name']

    # try:
    if age < 18:
        user.delete()
        raise AuthForbidden('social_core.backends.vk.VKOAuth2')

    if data['photo_200']:
        photo_link = data['photo_200']
        photo_response = requests.get(photo_link)
        path_photo = f'users_image/{user.pk}.jpg'
        with open(f'media/{path_photo}','wb') as photo:
            photo.write(photo_response.content)
        user.image = path_photo

    if data['personal']['langs']:
        lang_str = ''
        for ind, lang in enumerate(data['personal']['langs']):
            lang_str += f'{lang}' if ind == 0 else f', {lang}'
        user.userprofile.langs = lang_str

    user.save()


