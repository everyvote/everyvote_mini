from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'everyvote_mini.views.home', name='home'),
    # url(r'^everyvote_mini/', include('everyvote_mini.foo.urls')),
    (r'^$', 'logos.views.show_base'),
    
    url(r'^constituencies/all/$', 'logos.views.constituencies'),
    url(r'^constituencies/get/(?P<constituency_id>\d+)/$', 'logos.views.constituency'),
    
    url(r'^candidates/all/$', 'logos.views.candidates'),
    url(r'^candidates/get/(?P<candidate_id>\d+)$', 'logos.views.candidate'),
    
    url(r'^elections/all/$', 'logos.views.elections'),
    url(r'^elections/get/(?P<election_id>\d+)$', 'logos.views.election'),
    url(r'^elections/add/$', 'logos.views.add_election'),
    
    
    
    url(r'^accounts/login/$', 'everyvote_mini.views.login'),
    url(r'^accounts/auth/$', 'everyvote_mini.views.auth_view'),
    url(r'^accounts/logout/$', 'everyvote_mini.views.logout'),
    url(r'^accounts/loggedin/$', 'everyvote_mini.views.loggedin'),
    url(r'^accounts/invalid/$', 'everyvote_mini.views.invalid_login'),
    url(r'^accounts/register/$', 'everyvote_mini.views.register_user'),
    url(r'^accounts/register_success/$', 'everyvote_mini.views.register_success'),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    )
