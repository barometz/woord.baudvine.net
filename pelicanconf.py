AUTHOR = 'Dominic van Berkel'
SITENAME = 'woord'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['images', 'static']

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
SOCIAL = (
    ('Mastodon', 'https://tech.lgbt/@barometz'),
    ('Github', 'https://github.com/barometz'),
    )

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
PLUGINS = ['pelican-open_graph', 'i18n_subsites']
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
I18N_TEMPLATES_LANG = 'en'

I18N_SUBSITES = {
    'nl': {
        'SITENAME': 'woord',
    }
}

# Presentation
THEME = 'pelican-themes/pelican-bootstrap3'
CUSTOM_CSS = "static/woord.css"
BOOTSTRAP_THEME = 'flatly'
DOCUTIL_CSS = True
DEFAULT_LANG = 'en'

MARKDOWN['extension_configs']['markdown.extensions.codehilite']['linenums'] = True
