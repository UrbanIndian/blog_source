#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Janit Vora'
SITENAME = "Janit Vora's Blog"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Markdown Language Generator', 'https://pandao.github.io/editor.md/index.html'),
         ('Pelican Setup Blog','https://matthewdevaney.com/'),)
		

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/janitvora'),
          ('Github', 'https://github.com/UrbanIndian'),
          ('LinkedIn','https://www.linkedin.com/in/janitvora/'))

DEFAULT_PAGINATION = False

OUTPUT_PATH = '../output'
THEME = 'theme'
PLUGIN_PATHS = ['plugins/', ]
PLUGINS = ['i18n_subsites', ]
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}
BOOTSTRAP_THEME = 'flatly'
PYGMENTS_STYLE = 'monokai'

STATIC_PATHS = ['img', 'pdf']
PAGE_PATHS = ['pages']

ARTICLE_URL = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'

DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = ['CNAME']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True