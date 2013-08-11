from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'everyvote_mini.views.home', name='home'),
    # url(r'^everyvote_mini/', include('everyvote_mini.foo.urls')),
    (r'^$', 'evmini_reorganized.views.constituency.list'),
    )
