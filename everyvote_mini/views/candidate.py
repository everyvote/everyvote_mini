from everyvote_mini.models import Election, Candidate, UserProfile
from everyvote_mini.forms import CandidateForm
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render_to_response

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
    context_object_name = 'candidate'
    template_name = 'candidate_form.html'

# DELETE CANDIDATE
class CandidateDeleteView(DeleteView):
    model = Candidate
    success_url = reverse_lazy('home')
    template_name = 'candidate_delete.html'
    
