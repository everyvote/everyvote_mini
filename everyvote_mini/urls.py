from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from logos.views import ElectionListView, ElectionDetailView
from logos.views import ConstituencyListView, ConstituencyDetailView

from everyvote_mini.models import Constituency, Election
from member.views import MemberEditView
from django.contrib.auth.decorators import login_required


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^elections/all', ElectionListView.as_view(
        model=Election,
        template_name='election_list.html',
        context_object_name='election_list',
        )),
    
    url(r'^elections/get/(?P<pk>\d+)/$', ElectionDetailView.as_view(
        model=Election,
        template_name='election.html',
        context_object_name='election',
        )),
    
    url(r'^constituencies/all', ConstituencyListView.as_view(
        model=Constituency,
        template_name='constituency_list.html',
        context_object_name='constituency_list',
        )),
    
    url(r'^constituencies/get/(?P<pk>\d+)/$', ConstituencyDetailView.as_view(
        model=Constituency,
        template_name='constituency.html',
        context_object_name='constituency',
        )),
    

    
    # Examples:
    # url(r'^$', 'everyvote_mini.views.home', name='home'),
    # url(r'^everyvote_mini/', include('everyvote_mini.foo.urls')),
    (r'^$', 'logos.views.home'),
        
    url(r'^candidates/all/$', 'logos.views.candidates'),
    url(r'^candidates/get/(?P<candidate_id>\d+)/$', 'logos.views.candidate'),
    url(r'^candidates/add_candidate/$', 'logos.views.add_candidate'),
    url(r'^candidates/add_comment/(?P<candidate_id>\d+)/$', 'logos.views.add_comment'),

    #/ using ListView instead  url(r'^constituencies/all/$', 'logos.views.constituencies'),
    #/ using DetailView instead url(r'^constituencies/get/(?P<constituency_id>\d+)/$', 'logos.views.constituency'),
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

    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/', include('django.contrib.comments.urls')),
    
    )
