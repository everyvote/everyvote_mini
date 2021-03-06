from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from everyvote_mini.views.election import ElectionListView, ElectionDetailView, ElectionCreateView, ElectionUpdateView, ElectionDeleteView
from everyvote_mini.views.election import ElectionOfficeDetailView
from everyvote_mini.views.parent_constituency import ParentConstituencyCreateView, ParentConstituencyListView, ParentConstituencyDetailView, ParentConstituencyUpdateView, ParentConstituencyDeleteView
from everyvote_mini.views.constituency import ConstituencyListView, ConstituencyDetailView, ConstituencyCreateView, ConstituencyUpdateView, ConstituencyDeleteView
from everyvote_mini.views.office import OfficeCreateView, OfficeDetailView, OfficeUpdateView, OfficeDeleteView
from everyvote_mini.views.candidate import CandidateCreateView, CandidateDetailView, CandidateUpdateView, CandidateDeleteView
from everyvote_mini.views.user import UserProfileDetailView, UserProfileUpdateView
from everyvote_mini.models import ParentConstituency, Constituency, Office, Election, Candidate
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from registration.views import register
from everyvote_mini.forms import RegistrationFormUniqueEmail
admin.autodiscover()


# HOME PAGE
# PARENT CONSTITUENCIES (universities): create, list, show, update, delete
# CONSTITUENCIES (organizations): create, show, update, delete
# OFFICES: create, show, update, delete
# ELECTIONS: create, show-random, show-alphabetical, update, delete
# USERS AND AUTHENTICATION: login, logout, show, update
# CANDIDATES: create, show, update, delete
# REGISTRATION (with recaptcha)
# COMMENTS
# CONTACT
# ADMIN INTERFACE


urlpatterns = patterns('',

###
#HOME PAGE
###
# SHOW HOME PAGE
    url(r'^$', 'everyvote_mini.views.home.home', name='home'),

###
#PARENT CONSTITUENCIES (called 'universities' in the UI): create, list, show, update, delete
###
# CREATE PARENT CONSTITUENCY
    url(r'^universities/add/$', login_required(ParentConstituencyCreateView.as_view()),
        name='parent_constituency_create',),
# LIST PARENT CONSTITUENCIES
    url(r'^universities/all', ParentConstituencyListView.as_view(
        model=ParentConstituency,
        template_name='parent_constituency_list.html',
        context_object_name='parent_constituency_list',
        )),
# SHOW PARENT CONSTITUENCY
    url(r'^universities/(?P<pk>\d+)/$', ParentConstituencyDetailView.as_view(
        model=ParentConstituency,
        template_name='parent_constituency_detail.html',
        context_object_name='parent_constituency'),
        name='parent_constituency_detail',
        ),
# UPDATE PARENT CONSTITUENCY
    url(r'^universities/update/(?P<pk>\d+)/$', login_required(ParentConstituencyUpdateView.as_view()),
        name='parent_constituency_update',),
# DELETE PARENT CONSTITUENCY
    url(r'^universities/delete/(?P<pk>\d+)/$', login_required(ParentConstituencyDeleteView.as_view()),
        name='parent_constituency_delete',),
        
###
#CONSTITUENCIES (called 'organizations' in the UI): create, show, update, delete
###
# CREATE CONSTITUENCY
    url(r'^organizations/add/$', login_required(ConstituencyCreateView.as_view()),
        name='constituency_create',),
# SHOW CONSTITUENCY
    url(r'^organizations/(?P<pk>\d+)/$', ConstituencyDetailView.as_view(
        model=Constituency,
        template_name='constituency_detail.html',
        context_object_name='constituency'),
        name='constituency_detail',
        ),
# UPDATE CONSTITUENCY
    url(r'^organizations/update/(?P<pk>\d+)/$', login_required(ConstituencyUpdateView.as_view()),
        name='constituency_update',),
# DELETE CONSTITUENCY
    url(r'^organizations/delete/(?P<pk>\d+)/$', login_required(ConstituencyDeleteView.as_view()),
        name='constituency_delete',),

###
#OFFICES: create, show, update, delete
###
# CREATE OFFICE
    url(r'^offices/add/$', login_required(OfficeCreateView.as_view()),
        name='office_create',),
# SHOW OFFICE
    url(r'^offices/(?P<pk>\d+)/$', OfficeDetailView.as_view(
        model=Office,
        template_name='office_detail.html',
        context_object_name='office'),
        name='office_detail',
        ),
# UPDATE OFFICE
    url(r'^offices/update/(?P<pk>\d+)/$', login_required(OfficeUpdateView.as_view()),
        name='office_update',), 
# DELETE OFFICE
    url(r'^offices/delete/(?P<pk>\d+)/$', login_required(OfficeDeleteView.as_view()),
        name='office_delete',),

###
# ELECTIONS: create, show-random, show-alphabetical, update, delete
###
# CREATE ELECTION
    url(r'^elections/add/$', login_required(ElectionCreateView.as_view()),
        name='election_create',),
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
# SHOW ELECTION - SHOW ONLY ONE OFFICE
    url(r'^elections/(?P<pk>\d+)/office/(?P<office_id>\d+)/$', ElectionOfficeDetailView.as_view(
        model=Election,
        template_name='election_detail_by_office.html'),
        name='election_detail_by_office',
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
# MODERATOR CREATE CANDIDATE
    url(r'^candidates/mod-add/$', 'everyvote_mini.views.candidate.mod_create_candidate'),
# MODERATOR APPROVE CANDIDATE
    url(r'^candidates/mod-approve/(?P<num>\d+)/$', 'everyvote_mini.views.candidate.mod_approve_candidate'),
# MODERATOR DENY CANDIDATE
    url(r'^candidates/mod-deny/(?P<num>\d+)/$', 'everyvote_mini.views.candidate.mod_deny_candidate'),
# SHOW CANDIDATE
    url(r'^candidates/(?P<pk>\d+)/$', CandidateDetailView.as_view(
        model=Candidate,
        template_name='candidate_detail.html',
        context_object_name='candidate'),
        name='candidate_detail',
        ),
# SHOW PREVIOUS CANDIDATE
#    url(r'^candidates/(?P<id>\d+)/$', 'everyvote_mini.views.candidate.show_previous_candidate'),
# SHOW NEXT CANDIDATE
#    url(r'^candidates/(?P<id>\d+)/$', 'everyvote_mini.views.candidate.show_next_candidate'),
# UPDATE CANDIDATE
    url(r'^candidates/update/(?P<pk>\d+)/$', login_required(CandidateUpdateView.as_view()),
        name='candidate_update',),
# DELETE CANDIDATE
    url(r'^candidates/delete/(?P<pk>\d+)/$', login_required(CandidateDeleteView.as_view()),
        name='candidate_delete',),

###
# USERS: show, update
###    
# SHOW USER
    url(r'^users/(?P<slug>\w+)/$', UserProfileDetailView.as_view(),
        name='user_detail'),
# UPDATE USER
    url(r'^users/update/(?P<slug>\w+)/$', login_required(UserProfileUpdateView.as_view()),
        name='user_form'),

###
# REGISTRATION: register
# 
# NOTE: You will need to pip install django-registration
###
# REGISTER NEW USER, WITH RECAPTCHA
    (r'^accounts/register/$', 'registration.views.register',    {'form_class':RegistrationFormUniqueEmail,'backend': 'registration.backends.default.DefaultBackend'}),
    (r'^accounts/', include('registration.urls')),
# PASSWORD RESET
    (r'^accounts/changepassword/$', 'django.contrib.auth.views.password_change'),
    (r'^accounts/changepassword/done/&', 'django.contrib.auth.views.password_change_done'),
    (r'^accounts/resetpassword/passwordsent/$', 'django.contrib.auth.views.password_reset_done'),
    (r'^accounts/resetpassword/$', 'django.contrib.auth.views.password_reset'),
    (r'^accounts/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>,+)/$', 'django.contrib.auth.views.password_reset_confirm'),
    (r'^accounts/reset/done/$', 'django.contrib.auth.views.password_reset_complete'),
###
# COMMENTS
###
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^comments/delete/(?P<comment_id>\d+)/$', 'everyvote_mini.views.comment.delete'),

###
# CONTACT / THANKS FOR CONTACTING!
###
    url(r'^contact/$', 'everyvote_mini.views.contact.contact'),
    url(r'^thanks/$', 'everyvote_mini.views.contact.thanks'),

###
# ABOUT
###
    url(r'^about/$', 'everyvote_mini.views.about.about'),

###
# ADMIN INTERFACE
###
    url(r'^admin/', include(admin.site.urls)),

# URLS.PY CLOSING PARENTHISIS
)
