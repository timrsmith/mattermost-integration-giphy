# -*- coding: utf-8 -*-
import os

# username the bot posts as
USERNAME = os.environ.get('USERNAME', 'giphy')

# display picture the bot posts with
ICON_URL = os.environ.get('ICON_URL', 'https://api.giphy.com/img/api_giphy_logo.png')

# the maximum parental rating of gifs posted
RATING = os.environ.get('RATING', 'pg')

# scheme to be used for the gif url return to mattermost
SCHEME = os.environ.get('SCHEME', 'https')

# the is a public beta key from giphy api
GIPHY_API_KEY = os.environ.get('GIPHY_API_KEY', 'dc6zaTOxFJmzC')

# the Mattemost token generated when you created your outgoing webhook
MATTERMOST_GIPHY_TOKEN = os.environ.get('MATTERMOST_GIPHY_TOKEN', None)
