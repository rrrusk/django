from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
    url(r'^$', views.main),
    url(r'form', views.form),
    url(r'tube', views.tube),
    url(r'you', views.you),
)
