from django.contrib import admin, messages
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe

from .models import *


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    form = PostAdminForm
    list_display = ('id', 'title', 'slug', 'is_published', 'author', 'category', 'time_update', 'get_photo', 'views')
    list_display_links = ('id', 'title')
    list_editable = ('is_published', )
    save_as = True
    save_on_top = True
    fields = ('title', 'slug', 'content', 'photo', 'author', 'category', 'tags',
              'is_published', 'views', 'get_photo', 'time_create', 'time_update')
    readonly_fields = ('views', 'get_photo', 'time_create', 'time_update')
    filter_horizontal = ['tags']
    search_fields = ['title', 'category__name']
    list_filter = ['is_published', 'category__name', 'tags']
    ordering = ('-time_update', )
    list_per_page = 5
    actions = ['set_published', 'set_draft', ]

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        return '-'

    get_photo.short_description = 'Photo'

    @admin.action(description="Опубликовать выбранные записи")
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Post.Status.PUBLISHED)
        self.message_user(request, f"Изменено {count} записей.")

    @admin.action(description="Снять с публикации выбранные записи")
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Post.Status.DRAFT)
        self.message_user(request, f"{count} записей сняты с публикации.", messages.WARNING)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    save_as = True
    save_on_top = True
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    ordering = ('name',)
    list_per_page = 5


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    save_as = True
    save_on_top = True
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    ordering = ('name',)
    list_per_page = 5


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    save_as = True
    save_on_top = True
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    ordering = ('name',)
    list_per_page = 5
