import re
from django.conf.urls.defaults import url, patterns, include
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Poor man's flatpages..
    url(r'^$', 'core.views.direct_to_template', {'path': 'index'}, name='index'),
    url(r'^(?P<path>.*)/$', 'core.views.direct_to_template', name='page'),

    # Administrative components
    # url(r'^grappelli/', include('grappelli.urls')),
    # url(r'^admin/', include(admin.site.urls)),
)

# In production, these two locations must be served up statically
urlpatterns += patterns('django.views.static',
    url(r'^%s(?P<path>.*)$' % re.escape(settings.MEDIA_URL.lstrip('/')), 'serve', {
        'document_root': settings.MEDIA_ROOT
    }),
    url(r'^%s(?P<path>.*)$' % re.escape(settings.STATIC_URL.lstrip('/')), 'serve', {
        'document_root': settings.STATIC_ROOT
    }),
#    url(r'^(?P<path>.*)$', 'serve', {
#        'document_root': settings.DOCUMENT_ROOT
#    }),
)
