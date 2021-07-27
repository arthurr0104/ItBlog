from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from ItBlog.settings import DEBUG, MEDIA_URL, MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('user/', include('user.urls')),
    path('', include('contact.urls')),
    path('captcha/', include('captcha.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),

]

if DEBUG:
    import debug_toolbar
    import mimetypes

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
