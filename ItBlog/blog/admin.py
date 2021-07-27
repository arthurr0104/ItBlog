from django.contrib import admin

from mptt.admin import MPTTModelAdmin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

from .models import Post, Category, ImportantNews, Tag, Comment


class ImportantNewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_date', 'edited_date', 'is_published')
    list_display_links = ('id', 'title')


admin.site.register(ImportantNews, ImportantNewsAdmin)


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ('id', 'title', 'category', 'created_date', 'edited_date', 'views', 'is_top', 'is_published')
    list_display_links = ('id', 'title')
    list_filter = ('category', 'tag', 'created_date',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class TagAdmin(CategoryAdmin):
    pass


admin.site.register(Tag, TagAdmin)


class CustomMPTTModelAdmin(MPTTModelAdmin):
    # specify pixel amount for this ModelAdmin only:
    mptt_level_indent = 25
    list_display = ('id', 'post_id', 'author', 'parent', 'created_at', 'is_published',)
    exclude = ('author',)  # скрыть author поле, чтобы оно не отображалось в форме изменений

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.author = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Comment, CustomMPTTModelAdmin)
