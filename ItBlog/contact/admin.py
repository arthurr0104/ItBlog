from django.contrib import admin

from .models import AboutUs, ContactUs


class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_date', 'edited_date', 'is_published')
    list_display_links = ('id', 'title')


admin.site.register(AboutUs, AboutUsAdmin)


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'message', 'created_at')
    list_display_links = ('id', 'name')


admin.site.register(ContactUs, ContactUsAdmin)
