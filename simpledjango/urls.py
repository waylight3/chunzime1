from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'simpledjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'simple.views.index', name='index'),
    url(r'^home$', 'simple.views.home', name='home'),
    url(r'^conversation$', 'simple.views.conversation', name='conversation'),
)
