from django.contrib import admin
from django.utils.translation import gettext as _

from .models import Post, Category, Tag


class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'slug', 'excerpt', 'views', 'read_time',
        'is_published', 'published_date', 'modified_date',
        'author', 'category'
    ]
    search_fields = ['title', 'content']
    list_display_links = ['title']
    list_filter = ['is_published', 'published_date', 'modified_date']
    list_editable = ['is_published']

    fieldsets = [
        (_('admin_main_fields'), {
            'fields': (
                'title', 'content', 'is_published', 'image', 'category', 'tags'
            )
        }),
        (_('admin_additional_fields'), {
            'fields': ('slug', 'excerpt', 'author')
        })
    ]
    filter_horizontal = ['tags']
    prepopulated_fields = {'slug': ['title']}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'parent']
    search_fields = ['name']
    list_display_links = ['name']
    list_filter = ['parent']

    fieldsets = [
        (_('admin_main_fields'), {'fields': ('name', 'parent')}),
        (_('admin_additional_fields'), {'fields': ('slug',)})
    ]
    prepopulated_fields = {'slug': ['name']}


class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_display_links = ['name']


admin.site.site_title = _('admin_site_title')
admin.site.site_header = _('admin_site_header')

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
