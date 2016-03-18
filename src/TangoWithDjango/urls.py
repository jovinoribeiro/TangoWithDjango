from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
import leialater
import ranchomirage


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TangoWithDjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^rango/', include('rango.urls')),
    url(r'^leialater/', include('leialater.urls')),
    url(r'^ranchomirage/', include('ranchomirage.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )