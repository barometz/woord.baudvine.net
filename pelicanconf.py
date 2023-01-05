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

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('Mastodon', 'https://mastodon.lol/@barometz'),
          ('Github', 'https://github.com/barometz'),
          ('Twitter', 'https://twitter.com/baudvine'))

DEFAULT_PAGINATION = False

TWITTER_CARDS = True
TWITTER_USERNAME = 'baudvine'

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
THEME = 'pelican-sober'
PELICAN_SOBER_HOME_LISTS_ARTICLES = True
CSS_FILE = "woord.css" 
DEFAULT_LANG = 'en'

MARKDOWN['extension_configs']['markdown.extensions.codehilite']['linenums'] = True
