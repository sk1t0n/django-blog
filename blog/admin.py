from django.contrib import admin
from django.contrib.admin.views.main import ChangeList
from django.utils.translation import gettext as _, get_language

from .models import Post, Category, Tag


class CustomPostChangeList(ChangeList):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if get_language() == 'ru':
            self.title = 'Выберите статью для изменения'


class CustomCategoryChangeList(ChangeList):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if get_language() == 'ru':
            self.title = 'Выберите категорию для изменения'


def get_title_changeform_view(url: str, model_accusative_case: str) -> str:
    if url.endswith('/add/'):
        return f'Добавить {model_accusative_case}'
    else:
        return f'Изменить {model_accusative_case}'


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

    def get_changelist(self, request, **kwargs):
        return CustomPostChangeList

    def changeform_view(self, request, obj_id, form_url, extra_context=None):
        if get_language() == 'ru':
            extra_context = {} if extra_context is None else extra_context
            extra_context['title'] = get_title_changeform_view(request.path, 'статью')  # noqa
        return super(PostAdmin, self).changeform_view(
            request, obj_id, form_url, extra_context=extra_context
        )


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

    def get_changelist(self, request, **kwargs):
        return CustomCategoryChangeList

    def changeform_view(self, request, obj_id, form_url, extra_context=None):
        if get_language() == 'ru':
            extra_context = {} if extra_context is None else extra_context
            extra_context['title'] = get_title_changeform_view(request.path, 'категорию')  # noqa
        return super(CategoryAdmin, self).changeform_view(
            request, obj_id, form_url, extra_context=extra_context
        )


class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_display_links = ['name']


admin.site.site_title = _('site_title')
admin.site.site_header = _('admin_site_header')

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
