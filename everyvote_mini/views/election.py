from everyvote_mini.models import Election
from everyvote_mini.forms import ElectionForm
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

"""
ELECTION
"""
# CREATE ELECTION
class ElectionCreateView(CreateView):
    model = Election
    form_class = ElectionForm
    template_name = 'election_create.html'
    
    def form_valid(self, form):
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
    
    # I commented this out after I added the Parent Constituency class - Mitch
    # def get_context_data(self, **kwargs):
        
        # Obtain the context generating function from the parent class.
        # context = super(ElectionDetailView, self).get_context_data(**kwargs)

        # context['eligible_candidates'] = self.object.eligible_candidates()
        
        # return context
    
    
# UPDATE ELECTION
class ElectionUpdateView(UpdateView):
    model = Election
    form_class = ElectionForm
    template_name='election_form.html'

# DELETE ELECTION
class ElectionDeleteView(DeleteView):
    model = Election
    success_url = reverse_lazy('home')
    template_name='election_delete.html'
