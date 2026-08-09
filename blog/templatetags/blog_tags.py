from django import template
from blog.models import Post

register = template.Library()

@register.filter
def snippet(value, arg=100):
    return value[:arg] + ' ...'
