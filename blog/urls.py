from django.urls import path
from django.views.generic import detail

from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', home, name='home'),
    path('<int:pid>', single, name='single'),


]