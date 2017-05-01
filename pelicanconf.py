#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Jody M. Klymak'
SITENAME = 'UVic Ocean Physics'
SITEURL = 'http://web.uvic.ca/~jklyamk'

PATH = 'content'

TIMEZONE = 'Canada/Pacific'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ( ('U. of Victoria', 'http://uvic.ca/'),
          ('School of Earth and Ocean Sciences', 'http://seos.uvic.ca/'),
         ('Department of Physics & Astronomy', 'http://phys.uvic.ca/'),)

# Social widget
SOCIAL = (('Google Scholar', 'https://scholar.google.ca/citations?user=jiXa6MsAAAAJ&hl=en'),
          ('OrcID', 'http://orcid.org/0000-0003-4612-8600'),
          ('Github', 'http://github.com/jklymak'),)

DEFAULT_PAGINATION = 10

DEFAULT_DATE = 'fs'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

STATIC_PATHS = ['images','images/thumbnails', 'pdfs', 'pages/images','data']

PAGE_EXCLUDES = ['images','pdfs']

THEME = './themes/pelican-bootstrapJMK'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['pelican-bibtex','i18n_subsites','liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.vimeo',
           'liquid_tags.include_code', 'liquid_tags.notebook']
#BOOTSTRAP_FLUID = True
BOOTSTRAP_THEME = 'flatly'
DISPLAY_RECENT_POSTS_ON_SIDEBAR=True
DISPLAY_CATEGORIES_ON_MENU = False

SHOW_ARTICLE_AUTHOR = False
SHOW_ARTICLE_CATEGORY = True
SHOW_DATE_MODIFIED = True

SITELOGO = 'images/UvicOpgLogo.jpg'
SITELOGO_SIZE = '90px'

#BANNER = 'images/PrettyHeaderCrop.jpg'
#BANNER_ALL_PAGES = True
# BANNER_SUBTITLE = ''

TYPOGRIFY = True
SLUGIFY_SOURCE = 'basename'

PAGE_ORDER_BY = 'reversed-date'

### pubs_per_year
PUBLICATIONS_SRC = 'content/data/all.bib'
