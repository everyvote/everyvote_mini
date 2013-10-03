from everyvote_mini.models import Election
from everyvote_mini.forms import ElectionForm
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.http import Http404

"""
ELECTION
"""
# CREATE ELECTION
class ElectionCreateView(CreateView):
    model = Election
    form_class = ElectionForm
    template_name = 'election_create.html'

    def form_valid(self, form):
        if not form.instance.constituency.moderators.get(id = self.request.user.id).pk == self.request.user.id:
            raise Http404 # maybe you'll need to write a middleware to catch 403's same way
        f = form.save(commit=False)
        f.save()
        return super(ElectionCreateView, self).form_valid(form)
        
# LIST ELECTIONS
class ElectionListView(ListView):
    model = Election
    context_object_name = "elections"

# SHOW ELECTION
class ElectionDetailView(DetailView):
    model = Election
    context_object_name = "election"

    def get_context_data(self, **kwargs):
        
        # Obtain the context generating function from the parent class.
        context = super(ElectionDetailView, self).get_context_data(**kwargs)

        context['eligible_candidates'] = self.object.eligible_candidates()
        context['is_election_day'] = self.object.is_election_day()
        
        return context
        
# SHOW ELECTION PAGE WITH ONLY THE CANDIDATES RUNNING FOR ONE OFFICE
class ElectionOfficeDetailView(DetailView):
    model = Election
    context_object_name = "election"

    def get_context_data(self, **kwargs):
        context = super(ElectionOfficeDetailView, self).get_context_data(**kwargs)
        # At this point, the context contains the 'election' object
        election = context['election']
        # Add the 'office_candidates' to the context and use in the template.
        #   {% for candidate in office_candidates %}
        #       candidate
        #   {% endfor %}
        context['office_candidates'] = election.get_office_candidates(self.kwargs['office_id'])
        context['is_election_day'] = self.object.is_election_day()
        return context

# UPDATE ELECTION
class ElectionUpdateView(UpdateView):
    model = Election
    form_class = ElectionForm
    template_name='election_form.html'

    def get_object(self, *args, **kwargs):
        obj = super(ElectionUpdateView, self).get_object(*args, **kwargs)
        if not obj.constituency.moderators.get(id = self.request.user.id).pk == self.request.user.id:
            raise Http404 # maybe you'll need to write a middleware to catch 403's same way
        return obj
    
# DELETE ELECTION
class ElectionDeleteView(DeleteView):
    model = Election
    success_url = reverse_lazy('home')
    template_name='election_delete.html'
    
    def get_object(self, *args, **kwargs):
        obj = super(ElectionDeleteView, self).get_object(*args, **kwargs)
        if not obj.constituency.moderators.get(id = self.request.user.id).pk == self.request.user.id:
            raise Http404 # maybe you'll need to write a middleware to catch 403's same way
        return obj
