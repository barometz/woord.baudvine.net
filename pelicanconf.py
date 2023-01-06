AUTHOR = 'Dominic van Berkel'
SITENAME = 'woord'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['images', 'theme']

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# eevee has different feed constants for some reason
FEED_ATOM = 'feeds/all.atom.xml'

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('Mastodon', 'https://mastodon.lol/@barometz'),
          ('Github', 'https://github.com/barometz'),
          ('Twitter', 'https://twitter.com/baudvine'))

DEFAULT_PAGINATION = False

USE_OPEN_GRAPH = True
USE_TWITTER_CARDS = True
TWITTER_USERNAME = 'baudvine'

DISCLAIMER = 'Powered by love, rainbow sparkles, <a href="https://getpelican.com/">Pelican</a>, and <a href="https://kura.gg/eevee">Eevee</a>'
COPYRIGHT = 'All content © 2023 Dominic van Berkel'

# The default markdown config
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Plugins
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['pelican-open_graph']

# Presentation
THEME = 'eevee'
THEME_PRIMARY = 'light_green'
THEME_ACCENT = 'deep_orange'
DEFAULT_LANG = 'en'

# line numbers look like ass with the eevee theme.
# MARKDOWN['extension_configs']['markdown.extensions.codehilite']['linenums'] = True
