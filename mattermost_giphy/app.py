# -*- coding: utf-8 -*-
import os
import sys
import json
from urlparse import urlsplit
from urlparse import urlunsplit

import requests
from flask import Flask
from flask import request
from flask import Response

from mattermost_giphy.settings import *


app = Flask(__name__)


@app.route('/')
def root():
    """
    Home handler
    """

    return "OK"


@app.route('/new_post', methods=['POST'])
def new_post():
    """
    Mattermost new post event handler
    """

    data = request.form

    if MATTERMOST_GIPHY_TOKEN.find(data['token']) == -1:
        print('Tokens did not match, it is possible that this request came from somewhere other than Mattermost')
        return 'OK'

    # NOTE: support the slash command
    slash_command = False
    if 'command' in data:
        slash_command = True

    translate_text = data['text']
    if not slash_command:
        translate_text = data['text'][len(data['trigger_word']):]

    if len(translate_text) == 0:
        print("No translate text provided, not hitting Giphy")
        return 'OK'

    gif_url = giphy_translate(translate_text)

    if len(gif_url) == 0:
        print('No gif url found, not returning a post to Mattermost')
        return 'OK'

    resp_data = {}
    resp_data['text'] = '''`{}` searched for {}
{}'''.format(data.get('user_name', 'unknown').title(), translate_text, gif_url)
    resp_data['username'] = USERNAME
    resp_data['icon_url'] = ICON_URL
    if slash_command:
        resp_data['response_type'] = 'in_channel'

    resp = Response(content_type='application/json')
    resp.set_data(json.dumps(resp_data))

    return resp


def giphy_translate(text):
    """
    Giphy translate method, uses the Giphy API to find an appropriate gif url
    """

    params = {}
    params['s'] = text
    params['rating'] = RATING
    params['api_key'] = GIPHY_API_KEY

    resp = requests.get('https://api.giphy.com/v1/gifs/translate', params=params, verify=True)

    if resp.status_code is not requests.codes.ok:
        print('Encountered error using Giphy API, text=%s, status=%d, response_body=%s' % (text, resp.status_code, resp.json()))
        return ''

    resp_data = resp.json()

    url = list(urlsplit(resp_data['data']['images']['original']['url']))
    url[0] = SCHEME.lower()

    return urlunsplit(url)
