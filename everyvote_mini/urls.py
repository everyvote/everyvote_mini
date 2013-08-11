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
    url(r'^candidates/get/(?P<candidate_id>\d+)/$', 'logos.views.candidate'),
    url(r'^candidates/add_candidate/$', 'logos.views.add_candidate'),
    url(r'^candidates/add_comment/(?P<candidate_id>\d+)/$', 'logos.views.add_comment'),
    
    url(r'^elections/all/$', 'logos.views.elections'),
    url(r'^elections/get/(?P<election_id>\d+)/$', 'logos.views.election'),
    url(r'^elections/add_election/$', 'logos.views.add_election'),
    url(r'^offices/all/$', 'logos.views.all_offices'),
    
    url(r'^register/$', 'member.views.MemberRegistration'),
    url(r'^login/$', 'member.views.LoginRequest'),
    url(r'^logout/$', 'member.views.LogoutRequest'),
    url(r'^my_account/$', 'member.views.show_my_account'),
    url(r'^my_profiles/$', 'member.views.show_my_profiles'),
    
    url(r'^contact/$', 'logos.views.contact'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    )
