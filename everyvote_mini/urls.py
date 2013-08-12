from django.conf.urls import patterns, include, url

#/ mitch
#/
from logos.views import ElectionDetailView, ConstituencyDetailView
from django.views.generic import ListView, DetailView
from everyvote_mini.models import Constituency, Election
from member.views import MemberEditView
from django.contrib.auth.decorators import login_required
#/
#/ mitch

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    
    #/ mitch, trying to use ListView and DetailView in case we need to
    #/ add extra context aka add more than one model to a view's dictionary.
    #/ the old urls that these replace are commented-out below
    url(r'^elections/all', ListView.as_view(
        model=Election,
        template_name='elections.html',
        context_object_name="election_list",
        )),
    
    url(r'^elections/get/(?P<pk>\d+)/$', ElectionDetailView.as_view(
        model=Election,
        template_name='election.html',
        )),
    
    url(r'^constituencies/get/(?P<pk>\d+)/$', ConstituencyDetailView.as_view(
        model=Constituency,
        template_name='constituency.html',
        )),
    
    #/
    #/ mitch
    
    # Examples:
    # url(r'^$', 'everyvote_mini.views.home', name='home'),
    # url(r'^everyvote_mini/', include('everyvote_mini.foo.urls')),
    (r'^$', 'everyvote_mini.views.constituency.list'),
    
    url(r'^constituencies/all/$', 'logos.views.constituencies'),
#    url(r'^constituencies/get/(?P<constituency_id>\d+)/$', 'logos.views.constituency'),
    
    url(r'^candidates/all/$', 'logos.views.candidates'),
    url(r'^candidates/get/(?P<candidate_id>\d+)/$', 'logos.views.candidate'),
    url(r'^candidates/add_candidate/$', 'logos.views.add_candidate'),
    url(r'^candidates/add_comment/(?P<candidate_id>\d+)/$', 'logos.views.add_comment'),
    
    #/ using ListView instead   url(r'^elections/all/$', 'logos.views.elections'),
    #/ using DetailView instead url(r'^elections/get/(?P<election_id>\d+)/$', 'logos.views.election'),
    url(r'^elections/add_election/$', 'logos.views.add_election'),
    url(r'^offices/all/$', 'logos.views.all_offices'),
    
    url(r'^register/$', 'member.views.MemberRegistration'),
    url(r'^login/$', 'member.views.LoginRequest'),
    url(r'^logout/$', 'member.views.LogoutRequest'),
    url(r'^my_account/$', 'member.views.show_my_account'),
    url(r'^edit_member_profile/$', login_required(MemberEditView.as_view()), name='edit_member_profile'),
    url(r'^my_profiles/$', 'member.views.show_my_profiles'),
    
    url(r'^contact/$', 'logos.views.contact'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    )
