from django.contrib import admin
from django.conf import settings
from django.urls import path, re_path, include
from django.conf.urls import url
from django.views.generic import TemplateView
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^tinymce/', include('tinymce.urls')),
    re_path(r'^api_v0/', include('api_v0.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)

urlpatterns += [
    re_path(r'^.*$', include('frontend.urls'), name='frontend'),
]

if settings.DEBUG:
    urlpatterns += [url(r'^silk/', include('silk.urls', namespace='silk'))]