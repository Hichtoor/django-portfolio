from django.shortcuts import render

from blog.models import Post


# Create your views here.

def home(request):
    posts = Post.objects.filter(status=1)
    context = {'posts': posts}
    return render(request, 'blog/home.html', context)
