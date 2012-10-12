import re
from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def active(context, pattern, name='active', exact=True):
    """Returns a class name if pattern matches the current path.

    Usage:
        {% url "some-url" as some_url %}

        <a class="{% active url_stream %}" href="{{ url_stream }}">stream</a>
    """
    if exact:
        pattern = '^{}$'.format(pattern)
    if re.match(pattern, context['request'].path):
        return name
    return ''
