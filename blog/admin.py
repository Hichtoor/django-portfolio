from django.contrib import admin

from blog.models import Post


# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'published_at'
    list_display = ('title', 'content', 'status', 'published_at')
    list_filter = ('status',)
    search_fields = ('title', 'content')
    empty_value_display = '-empty-'