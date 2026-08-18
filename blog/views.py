from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def home(request, cat_name=None, author_name=None):
    posts = Post.objects.filter(status=1)
    if cat_name:
        posts = posts.filter(category__name=cat_name)
    if author_name:
        posts = posts.filter(author__username=author_name)

    posts = Paginator(posts, 3)

    try :
        page = request.GET.get('page')
        posts = posts.get_page(page)

    except PageNotAnInteger:
        posts = posts.get_page(1)

    except EmptyPage:
        posts = posts.get_page(1)

    context = {'posts': posts}

    return render(request, 'blog/home.html', context)

def single(request, pid=None, category=None):
    post = get_object_or_404(Post, pk=pid, status=1)
    context = {'post': post}
    return render(request, 'blog/single.html', context)


def search(request):
    posts = Post.objects.filter(status=1)

    if request.method == "GET":
        posts = posts.filter(content__contains=request.GET.get('s'))
        context = {'posts': posts}
    return render(request, 'blog/home.html', context)
