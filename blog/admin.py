from django.contrib import admin

from blog.models import Post, Category


# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'published_at'
    list_display = ('title', 'author', 'status', 'published_at')
    list_filter = ('status',)
    search_fields = ('title', 'content')
    empty_value_display = '-empty-'