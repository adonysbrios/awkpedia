from functools import partial

## https://github.com/neutronX/django-markdownx/issues/163#issuecomment-541420377

from django.conf import settings
from django.utils.safestring import mark_safe

import markdown
import bleach

bleach.sanitizer.ALLOWED_TAGS = frozenset({'p', 'table', 'sup', 'thead', 'tbody', 'tr', 'th', 'td', 'img', 'hr', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'br', 'ol', 'a', 'abbr', 'acronym', 'b', 'blockquote', 'code', 'em', 'i', 'li', 'ol', 'strong', 'ul'})
bleach.sanitizer.ALLOWED_ATTRIBUTES = {'a': ['class', 'href', 'title', 'id'], 'sup':['id'], 'h1':['id'], 'img': ['src'], 'li':['id'], 'abbr': ['title'], 'acronym': ['title']}
bleach.sanitizer.ALLOWED_PROTOCOLS = frozenset({'http', 'https'})

def markdownify(text):

    # Bleach settings
    whitelist_tags = getattr(settings, 'MARKDOWNIFY_WHITELIST_TAGS', bleach.sanitizer.ALLOWED_TAGS)
    whitelist_attrs = getattr(settings, 'MARKDOWNIFY_WHITELIST_ATTRS', bleach.sanitizer.ALLOWED_ATTRIBUTES)
    whitelist_protocols = getattr(settings, 'MARKDOWNIFY_WHITELIST_PROTOCOLS', bleach.sanitizer.ALLOWED_PROTOCOLS)

    extensions_conf = getattr(settings, "MARKDOWNX_MARKDOWNIFY_EXTENSION_CONFIGS", {})
    # Markdown settings
    strip = getattr(settings, 'MARKDOWNIFY_STRIP', True)
    extensions = getattr(settings, 'MARKDOWNIFY_MARKDOWN_EXTENSIONS', [])

    # Bleach Linkify
    linkify = None
    linkify_text = getattr(settings, 'MARKDOWNIFY_LINKIFY_TEXT', True)

    if linkify_text:
        linkify_parse_email = getattr(settings, 'MARKDOWNIFY_LINKIFY_PARSE_EMAIL', False)
        linkify_callbacks = getattr(settings, 'MARKDOWNIFY_LINKIFY_CALLBACKS', None)
        linkify_skip_tags = getattr(settings, 'MARKDOWNIFY_LINKIFY_SKIP_TAGS', None)
        linkifyfilter = bleach.linkifier.LinkifyFilter

        linkify = [partial(linkifyfilter,
                callbacks=linkify_callbacks,
                skip_tags=linkify_skip_tags,
                parse_email=linkify_parse_email
                )]

    # Convert markdown to html
    html = markdown.markdown(text, extensions=extensions, extension_configs=extensions_conf)
    # Sanitize html if wanted
    if getattr(settings, 'MARKDOWNIFY_BLEACH', True):

        cleaner = bleach.Cleaner(tags=whitelist_tags,
                                 attributes=whitelist_attrs,
                                 protocols=whitelist_protocols,
                                 strip=strip,
                                 filters=linkify,
                                 )

        html = cleaner.clean(html)

    return mark_safe(html)