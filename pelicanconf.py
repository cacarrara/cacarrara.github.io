#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Caio Carrara'
AUTHOR_EMAIL = u'caiocarrara@gmail.com'
SITENAME = u'Caio Carrara Log'
SITEURL = 'http://caiocarrara.com.br'

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'pt'

USE_FOLDER_AS_CATEGORY = True

DEFAULT_METADATA = (
    ('About_author', 'Trabalhando principalmente com Python, Java, HTML, CSS e Javascript. Hora ou outra me arrisco no empreendedorismo. Quando não estou programando ou estudando estou treinando, andando de bicicleta, jogando meu 3DS ou assistindo um filme.'),
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

PLUGIN_PATHS = ['pelican-plugins',]

PLUGINS = [
    'sitemap',
    'gravatar',
    'gzip_cache', #keep this as last plugin
]

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

PAGE_URL = PAGE_SAVE_AS = '{slug}.html'

THEME = 'themes/pure'
COVER_IMG_URL = 'http://i.imgur.com/uZIQDHD.jpg'
TAGLINE = 'Falando sobre desenvolvimento de software com destaque para Python, Django, Java, VRaptor, web e Agile.'
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

STATIC_PATHS = ['images', 'extra/CNAME',]
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}
