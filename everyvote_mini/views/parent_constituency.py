from everyvote_mini.models import ParentConstituency
from everyvote_mini.forms import ParentConstituencyForm
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

"""
PARENT CONSTITUENCY
"""

# LIST PARENT CONSTITUENCY
class ParentConstituencyListView(ListView):
    model = ParentConstituency

# SHOW PARENT CONSTITUENCY
class ParentConstituencyDetailView(DetailView):
    model = ParentConstituency
    context_object_name = "parent_constituency"

# CREATE PARENT CONSTITUENCY
class ParentConstituencyCreateView(CreateView):
    model = ParentConstituency
    form_class = ParentConstituencyForm
    template_name = 'parent_constituency_create.html'
    
    def form_valid(self, form):
        f = form.save(commit=False)
        f.save()
        return super(ParentConstituencyCreateView, self).form_valid(form)

# UPDATE PARENT CONSTITUENCY
class ParentConstituencyUpdateView(UpdateView):
    model = ParentConstituency
    form_class = ParentConstituencyForm
    template_name='parent_constituency_form.html'

# DELETE PARENT CONSTITUENCY
class ParentConstituencyDeleteView(DeleteView):
    model = ParentConstituency
    success_url = reverse_lazy('home')
    template_name='parent_constituency_delete.html'