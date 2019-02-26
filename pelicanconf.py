#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Govind KP'
SITENAME = 'reisub0'
SITEURL = ''

PATH = 'content'
OUTPUT_PATH = 'public'
STATIC_PATHS = [
    # 'images',
    'extra',  # this
]

PLUGIN_PATHS = ['plugins']
PLUGINS = ['sitemap']

EXTRA_PATH_METADATA = {
    # 'extra/custom.css': {'path': 'custom.css'},
    'extra/robots.txt': {
        'path': 'robots.txt'
    },
    'extra/logo.jpg': {
        'path': 'logo.jpg'
    },
    'extra/favicon.ico': {
        'path': 'favicon.ico'
    },
    'extra/CNAME': {
        'path': 'CNAME'
    },
    'extra/LICENSE': {
        'path': 'LICENSE'
    },
    'extra/README': {
        'path': 'README'
    },
}

THEME = './theme/pelican-svbhack'
USER_LOGO_URL = SITEURL + '/logo.jpg'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (('Github', 'https://github.com/reisub0/'), )

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
