from everyvote_mini.models import Election, Candidate, UserProfile
from everyvote_mini.forms import CandidateForm, UserCreateForm
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth.models import User
from django.template import RequestContext
from datetime import datetime

"""
CANDIDATE
"""
# CREATE CANDIDATE
class CandidateCreateView(CreateView):
    model = Candidate
    form_class = CandidateForm
    template_name = 'candidate_create.html'

    def form_valid(self, form):
        candidate = form.save(commit=False)
        candidate.user = UserProfile.objects.get(user=self.request.user) # use your own profile here
        candidate.save()
        return super(CandidateCreateView, self).form_valid(form)

# MODERATOR APPROVE CANDIDATE
def mod_approve_candidate(request, num="0"):
    candidate = get_object_or_404(Candidate, id=num)
    if request.user in candidate.election.constituency.moderators.filter(username=request.user):
        candidate.is_approved = True
        candidate.save()
        election = candidate.election
        return redirect(election)
    else:
        raise Http404

# MODERATOR DENY CANDIDATE
def mod_deny_candidate(request, num="0"):
    candidate = get_object_or_404(Candidate, id=num)
    if request.user in candidate.election.constituency.moderators.filter(username=request.user):
        candidate.is_approved = False
        candidate.save()
        election = candidate.election
        return redirect(election)
    else:
        raise Http404

# MODERATOR CREATE CANDIDATE
def mod_create_candidate(request):
    if request.method == "POST":
        uform = UserCreateForm(request.POST, instance=User())
        cform = CandidateForm(request.POST, instance=Candidate())
        if uform.is_valid() and cform.is_valid():
            new_user = uform.save(commit=False)
            new_candidate = cform.save(commit=False)
            if request.user in new_candidate.election.constituency.moderators.filter(username=request.user):
                new_user.last_login = datetime.now()
                new_user.date_joined = datetime.now()
                new_user.is_active = True
                new_user.save()
                new_user.userprofile.first_name = new_user.first_name
                new_user.userprofile.last_name = new_user.last_name
                new_user.userprofile.save()
                new_candidate.user = new_user.userprofile
                new_candidate.is_approved = True
                new_candidate.save()
                return HttpResponseRedirect('/candidates/mod-add/')
            else:
                raise Http404 # maybe you'll need to write a middleware to catch 403's same way
    else:
        uform = UserCreateForm(instance=User())
        cform = CandidateForm(instance=Candidate())
    return render_to_response('candidate_mod_create.html', {'user_form': uform, 'candidate_form': cform}, context_instance=RequestContext(request))
            
            
# SHOW CANDIDATE
class CandidateDetailView(DetailView):
    model = Candidate
    context_object_name = 'candidate'
    
    def get_context_data(self, **kwargs):
        context = super(CandidateDetailView, self).get_context_data(**kwargs)
        context['election'] = self.get_object().election
        return context

# UPDATE CANDIDATE
class CandidateUpdateView(UpdateView):
    model = Candidate
    form_class = CandidateForm
    context_object_name = 'candidate'
    template_name = 'candidate_form.html'
    
    def form_valid(self, form):
        candidate = form.save(commit=False)
        candidate.user = UserProfile.objects.get(user=self.request.user) # use your own profile here
        candidate.save()
        return super(CandidateUpdateView, self).form_valid(form)

    def get_object(self, *args, **kwargs):
        obj = super(CandidateUpdateView, self).get_object(*args, **kwargs)
        if not obj.user.id == self.request.user.userprofile.id:
            raise Http404 # maybe you'll need to write a middleware to catch 403's same way
        return obj
        
# DELETE CANDIDATE
class CandidateDeleteView(DeleteView):
    model = Candidate
    success_url = reverse_lazy('home')
    template_name = 'candidate_delete.html'
    
    def get_object(self, *args, **kwargs):
        obj = super(CandidateDeleteView, self).get_object(*args, **kwargs)
        if not obj.user.id == self.request.user.userprofile.id:
            raise Http404 # maybe you'll need to write a middleware to catch 403's same way
        return obj
    
