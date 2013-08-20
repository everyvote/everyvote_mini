from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from everyvote_mini.views.election import ElectionListView, ElectionDetailView, ElectionCreateView, ElectionUpdateView, ElectionDeleteView
from everyvote_mini.views.parentconstituency import ParentConstituencyListView, ParentConstituencyDetailView
from everyvote_mini.views.constituency import ConstituencyListView, ConstituencyDetailView, ConstituencyCreateView, ConstituencyUpdateView, ConstituencyDeleteView
from everyvote_mini.views.candidate import CandidateCreateView, CandidateDetailView, CandidateUpdateView, CandidateDeleteView
from everyvote_mini.views.user import UserProfileDetailView, UserProfileUpdateView
from everyvote_mini.models import ParentConstituency, Constituency, Election, Candidate
from django.contrib.auth.decorators import login_required
from django.contrib import admin
admin.autodiscover()

# HOME PAGE
# PARENT CONSTITUENCIES: list, show
# CONSTITUENCIES: create, list, show, update, delete
# ELECTIONS: create, list, show, update, delete
# USERS AND AUTHENTICATION: login, logout, show, update
# CANDIDATES: create, show, update, delete
# REGISTRATION
# COMMENTS
# CONTACT
# ADMIN INTERFACE


urlpatterns = patterns('',

###
# HOME PAGE
###
    url(r'^$', 'everyvote_mini.views.home.home', name='home'),

###
# PARENT CONSTITUENCIES
###

# LIST PARENTCONSTITUENCIES
    url(r'^parentconstituencies/all', ParentConstituencyListView.as_view(
        model=ParentConstituency,
        template_name='parentconstituency_list.html',
        context_object_name='parentconstituency_list',
        )),
# SHOW PARENTCONSTITUENCY
    url(r'^parentconstituencies/(?P<pk>\d+)/$', ParentConstituencyDetailView.as_view(
        model=ParentConstituency,
        template_name='parentconstituency_detail.html',
        context_object_name='parentconstituency'),
        name='parentconstituency_detail',
        ),

###
# CONSTITUENCIES: list, show
###

# CREATE CONSTITUENCY
    url(r'^constituencies/add/$', login_required(ConstituencyCreateView.as_view()),
        name='constituency_create',),
# LIST CONSTITUENCIES
    url(r'^constituencies/all', ConstituencyListView.as_view(
        model=Constituency,
        template_name='constituency_list.html',
        context_object_name='constituency_list',
        )),
# SHOW CONSTITUENCY
    url(r'^constituencies/(?P<pk>\d+)/$', ConstituencyDetailView.as_view(
        model=Constituency,
        template_name='constituency_detail.html',
        context_object_name='constituency'),
        name='constituency_detail',
        ),
# UPDATE CONSTITUENCY
    url(r'^constituencies/update/(?P<pk>\d+)/$', login_required(ConstituencyUpdateView.as_view()),
        name='constituency_update',),
# DELETE CONSTITUENCY
    url(r'^constituencies/delete/(?P<pk>\d+)/$', login_required(ConstituencyDeleteView.as_view()),
        name='constituency_delete',),

###
# ELECTIONS: create, list, show, update, delete
###

# CREATE ELECTION
    url(r'^elections/add/$', login_required(ElectionCreateView.as_view()),
        name='election_create',),
# LIST ELECTIONS
    url(r'^elections/all', ElectionListView.as_view(
        model=Election,
        template_name='election_list.html',
        context_object_name='election_list',
        )),
# SHOW ELECTION - RANDOM CANDIDATES
    url(r'^elections/(?P<pk>\d+)/$', ElectionDetailView.as_view(
        model=Election,
        template_name='election_detail.html',
        context_object_name='election'),
        name='election_detail',
        ),
# SHOW ELECTION - ALPHABETICAL CANDIDATES
    url(r'^elections/(?P<pk>\d+)/alpha/$', ElectionDetailView.as_view(
        model=Election,
        template_name='election_detail_alpha.html',
        context_object_name='election'),
        name='election_detail_alpha',
        ),
# UPDATE ELECTION
    url(r'^elections/update/(?P<pk>\d+)/$', login_required(ElectionUpdateView.as_view()),
        name='election_update',),
# DELETE ELECTION
    url(r'^elections/delete/(?P<pk>\d+)/$', login_required(ElectionDeleteView.as_view()),
        name='election_delete',),

###
# CANDIDATES: create, show, update, delete
###

# CREATE CANDIDATE
    url(r'^candidates/add/$', login_required(CandidateCreateView.as_view()),
        name='candidate_create',),
# SHOW CANDIDATE
    url(r'^candidates/(?P<pk>\d+)/$', CandidateDetailView.as_view(
        model=Candidate,
        template_name='candidate_detail.html',
        context_object_name='candidate'),
        name='candidate_detail',
        ),
# UPDATE CANDIDATE
    url(r'^candidates/update/(?P<pk>\d+)/$', login_required(CandidateUpdateView.as_view()),
        name='candidate_update',),
# DELETE CANDIDATE
    url(r'^candidates/delete/(?P<pk>\d+)/$', login_required(CandidateDeleteView.as_view()),
        name='candidate_delete',),

###
# USERS AND AUTHENTICATION: login, logout, show, update
###

# LOGIN
    url(r'^login/$', 'django.contrib.auth.views.login',
        {'template_name': 'login.html'}, name='login'),
# LOGOUT
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login',
        name='logout'),    
# SHOW USER
    url(r'^users/(?P<slug>\w+)/$', UserProfileDetailView.as_view(),
        name='profile'),
# UPDATE USER
    url(r'^edit_profile/', login_required(UserProfileUpdateView.as_view()),
        name='edit_profile'),

###
# REGISTRATION: register
# The user registration system is an installed app (in settings.py) designed by Arun Ravindran,
# and you need to pip install it in order for everyvote_mini to work.
# Type into your console: pip install git+git://github.com/arocks/django-registration-1.5.git
###
    url(r'^accounts/', include('registration.backends.simple.urls')),

###
# COMMENTS
###
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^comments/delete/(?P<comment_id>\d+)/$', 'everyvote_mini.views.comment.delete'),

###
# CONTACT
###
    url(r'^contact/$', 'everyvote_mini.views.contact.contact'),

###
# ADMIN INTERFACE
###
    url(r'^admin/', include(admin.site.urls)),

# URLS.PY CLOSING PARENTHISIS
)
