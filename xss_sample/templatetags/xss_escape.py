from django import template
from django.template.defaultfilters import stringfilter
from django.utils.html import escape
import urllib

from django.utils.http import urlencode
from django.utils.safestring import mark_safe

register = template.Library()


def escape_any_non_alphanumeric_below_256_ascii(value):
    output = ""
    for char in value:
        if char.isalnum():
            output += char
        else:
            if ord(char) < 256:  # ord gets the ascii value
                output += "&#" + str(ord(char))+";"
            else:
                output += char
    return output


@register.filter(name='html_escape', is_safe=True)
@stringfilter
def html_escape(value):
    escaped = escape(value)
    return mark_safe(escaped.replace("/", "&#x2F;"))


@register.filter(name='css_escape', is_safe=True)
@stringfilter
def css_escape(value):
    return mark_safe(escape_any_non_alphanumeric_below_256_ascii(value))


@register.filter(name='attr_escape', is_safe=True)
@stringfilter
def attr_escape(value):
    return mark_safe(escape_any_non_alphanumeric_below_256_ascii(value))


@register.filter(name='js_escape', is_safe=True)
@stringfilter
def css_escape(value):
    return mark_safe(escape_any_non_alphanumeric_below_256_ascii(value))


@register.filter(name='url_escape', is_safe=True)
@stringfilter
def url_escape(value):
    try:
        return mark_safe(urlencode(value))
    except:
        return ""  # not a valid url
