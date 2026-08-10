from django import template
from blog.models import Post, Category

register = template.Library()

@register.filter
def snippet(value, arg=100):
    return value[:arg] + ' ...'

@register.inclusion_tag('blog/latest-posts.html')
def latest_posts(arg=3):
    posts = Post.objects.filter(status=True).order_by('-published_at')[:arg]
    return {'posts': posts}

@register.inclusion_tag('blog/post-categories.html')
def post_categories():
        posts = Post.objects.filter(status=True)
        categories = Category.objects.all()
        cat_dict = {}
        for name in categories:
            cat_dict[name] = posts.filter(category=name).count()

        return {'categories': cat_dict}
