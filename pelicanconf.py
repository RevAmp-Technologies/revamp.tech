#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'RevAmp Technologies'
SITENAME = u'RevAmp Technologies'
SITEURL = u'http://revamp.tech'

PATH = 'content'
STATIC_PATHS = ['images',
                'fonts',
                'css',
                'js',
                ]

PAGE_DIR = 'pages'
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}/index.html'

PAGE_ORDER_BY = 'basename'


ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{slug}.html'



TIMEZONE = 'Asia/Jerusalem'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('facebook', 'https://www.facebook.com/RevAmpTech'),
          ('twitter', 'https://twitter.com/revamptech'),
          ('github', 'https://revamp-technologies.github.io/'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False


THEME = "twenty-html5up"

# Needed by the twenty-html5up theme
def sidebar(value):
  if value.startswith('archives') or value.startswith('category'):
    return 'right-sidebar'
  elif value == 'index':
    return 'index'
  else:
    return 'no-sidebar'

JINJA_FILTERS = { 'sidebar': sidebar }

# Added for revamp.tech
TYPOGRIFY = True
MENUITEMS = [('Home', '/index.html')]
DIRECT_TEMPLATES = ['index']