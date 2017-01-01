from django.conf import settings

# Imgur API Keys
DRACEDITOR_IMGUR_CLIENT_ID = getattr(
    settings, 'DRACEDITOR_IMGUR_CLIENT_ID', ''
)
DRACEDITOR_IMGUR_API_KEY = getattr(
    settings, 'DRACEDITOR_IMGUR_API_KEY', ''
)

# Safe Mode
DRACEDITOR_MARKDOWN_SAFE_MODE = getattr(
    settings, 'DRACEDITOR_MARKDOWN_SAFE_MODE', True
)

# Markdownify
DRACEDITOR_MARKDOWNIFY_FUNCTION = getattr(
    settings, 'DRACEDITOR_MARKDOWNIFY_FUNCTION', 'draceditor.utils.markdownify'
)
DRACEDITOR_MARKDOWNIFY_URL = getattr(
    settings, 'DRACEDITOR_MARKDOWNIFY_URL', '/draceditor/markdownify/'
)

# Markdown extensions
DRACEDITOR_MARKDOWN_EXTENSIONS = getattr(
    settings, 'DRACEDITOR_MARKDOWN_EXTENSIONS', [
        'markdown.extensions.extra',
        'markdown.extensions.nl2br',
        'markdown.extensions.smarty',
        'markdown.extensions.fenced_code',

        # Custom markdown extensions.
        'draceditor.extensions.urlize',
        'draceditor.extensions.mention',
        'draceditor.extensions.emoji',
    ]
)

# Markdown Extensions Configs
DRACEDITOR_MARKDOWN_EXTENSION_CONFIGS = getattr(
    settings, 'DRACEDITOR_MARKDOWN_EXTENSION_CONFIGS', {}
)

# Markdown urls
DRACEDITOR_UPLOAD_URL = getattr(
    settings, 'DRACEDITOR_UPLOAD_URL', '/draceditor/uploader/'
)
DRACEDITOR_SEARCH_USERS_URL = getattr(
    settings, 'DRACEDITOR_SEARCH_USERS_URL', '/draceditor/search-user/'
)

# Markdown Extensions
DRACEDITOR_MARKDOWN_BASE_EMOJI_URL = getattr(
    settings, 'DRACEDITOR_MARKDOWN_BASE_EMOJI_URL', 'https://assets-cdn.github.com/images/icons/emoji/'
)
DRACEDITOR_MARKDOWN_BASE_MENTION_URL = getattr(
    settings, 'DRACEDITOR_MARKDOWN_BASE_MENTION_URL', 'https://forum.dracos-linux.org/profile/'
)
