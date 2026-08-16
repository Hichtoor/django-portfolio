from django.urls import path
from blog.views import *

from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', home, name='home'),
    path('<int:pid>', single, name='single'),
    path('category/<str:cat_name>', home, name='category'),
    path('author/<str:author_name>', home, name='author'),
    path('search/', search, name='search'),



]