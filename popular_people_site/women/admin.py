from django.contrib import admin, messages
from django.utils.safestring import mark_safe

from .models import *


class MerriedFilter(admin.SimpleListFilter):
    title = 'Статус женщины'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return [
            ('married', 'Замужем'),
            ('single', 'Не замужем')
        ]

    def queryset(self, request, queryset):
        if self.value() == 'married':
            return queryset.filter(husband__isnull=False)
        elif self.value() == 'single':
            return queryset.filter(husband__isnull=True)


@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'content', 'photo', 'post_photo', 'cat', 'husband', 'tags']
    # exclude = ['tags', 'is_published']
    readonly_fields = ['post_photo']
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ['tags']
    list_display = ('id', 'title', 'post_photo', 'time_create', 'is_published', 'cat')
    list_display_links = ('title',)
    ordering = ['-time_create', 'title']
    list_editable = ('is_published',)
    list_per_page = 7
    actions = ['set_published', 'set_draft']
    search_fields = ['title__startswith', 'cat__name']
    list_filter = [MerriedFilter, 'cat__name', 'is_published']
    save_on_top = True

    @admin.display(description='Текущее фото', ordering='content')
    def post_photo(self, women: Women):
        if women.photo:
            return mark_safe(f'<img src="{women.photo.url}" width=50>')
        else:
            return 'Без фото'

    @admin.action(description='Опубликовать выбранные записи')
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Women.Status.PUBLISHED)
        self.message_user(request, f'Опубликовано {count} записей.')

    @admin.action(description='Снять с публикации')
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Women.Status.DRAFT)
        self.message_user(request, f'{count} записей снято с публикации.', messages.WARNING)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    ordering = ['name']


@admin.register(Husband)
class HusbandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'm_count')
    list_display_links = ('id', 'name')
    ordering = ['name']


@admin.register(TagPost)
class TagPostdAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag', 'slug')
    list_display_links = ('id', 'tag')
    ordering = ['tag']
    prepopulated_fields = {'slug': ('tag',)}
