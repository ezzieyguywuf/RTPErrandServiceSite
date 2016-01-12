#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = 'Wolfgang E. Sanyer'
SITENAME = 'Tutorial'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'EST'

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
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
LOAD_CONTENT_CACH = False
# Flex is nice, has room for a portrait
# Casper2Pelican is very very nice, with a nice image up top
# syte theme error
# backdrop theme error
# twenty-htlm5up error
# nest is decent
# tanisha likes bt3-flat
# w3-personal-blog is nice
# bricks is a conteder
# mediumfox is very nice
# hyde is kinda nice
THEME = '/home/wolfie/Program/pelican-themes/.git'
TAGS_SAVE_AS = ''
TAG_SAVE_AS  = ''
