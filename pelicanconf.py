#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Caio Carrara'
AUTHOR_EMAIL = u'eu@caiocarrara.com.br'
SITENAME = u'Caio Carrara'
SITEURL = 'http://caiocarrara.com.br'

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'pt'

USE_FOLDER_AS_CATEGORY = True

DEFAULT_METADATA = (
    ('about_author', 'Programador para o resto da vida. Falando sobre software e a vida.'),
    ('author_g_plus_id', '108931761041773828029'),
)

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

MENUITEMS = [
    ('Arquivo', 'archives.html'),
    ('Sobre', 'sobre.html'),
    ('Contato', 'contato.html'),
]

SOCIAL = (
    ('github', 'https://github.com/cacarrara/'),
    ('twitter-square', 'https://twitter.com/CaioWCC'),
    ('rss', 'http://caiocarrara.com.br/feeds/caio-carrara.atom.xml'),
)

PLUGIN_PATHS = ['pelican-plugins', ]

PLUGINS = [
    'sitemap',
    'gravatar',
    'share_post',
    'gzip_cache',  # keep this as last plugin
]

DEFAULT_PAGINATION = 7

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

PAGE_URL = PAGE_SAVE_AS = '{slug}.html'

THEME = 'themes/pure'
COVER_IMG_URL = 'http://i.imgur.com/uZIQDHD.jpg'
TAGLINE = (
    'Desenvolvimento de software, Python, Internet Livre, negócios e ideias aleatórias. Não necessariamente nessa ordem'
)
GITHUB_URL = 'https://github.com/cacarrara/cacarrara.github.io'
DISQUS_SITENAME = 'caiocarrara'
GOOGLE_ANALYTICS = 'UA-28003582-1'

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.8,
        'indexes': 0.5,
        'pages': 0.3
    },
    'changefreqs': {
        'articles': 'daily',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

STATIC_PATHS = ['images', 'extra/CNAME', ]
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, }
