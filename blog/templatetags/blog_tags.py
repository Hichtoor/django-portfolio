from django import template
from blog.models import Post

register = template.Library()

@register.filter
def snippet(value, arg=100):
    return value[:arg] + ' ...'

@register.inclusion_tag('blog/latest-posts.html')
def latest_posts(arg=3):
    posts = Post.objects.filter(status=True).order_by('-published_at')[:arg]
    return {'posts': posts}