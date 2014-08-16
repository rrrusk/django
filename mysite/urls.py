from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^polls/', include('polls.urls')),
    (r'^tube/', include('polls.urls')),
    (r'^admin/', include(admin.site.urls)),
)
