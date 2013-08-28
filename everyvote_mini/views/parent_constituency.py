from everyvote_mini.models import ParentConstituency
from everyvote_mini.forms import ParentConstituencyForm
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.http import Http404

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
    
    def get_object(self, *args, **kwargs):
        obj = super(ParentConstituencyUpdateView, self).get_object(*args, **kwargs)
        if not obj.administrators.get(id = self.request.user.id).pk == self.request.user.id:
            raise Http404 # maybe you'll need to write a middleware to catch 403's same way
        return obj
    
# DELETE PARENT CONSTITUENCY
class ParentConstituencyDeleteView(DeleteView):
    model = ParentConstituency
    success_url = reverse_lazy('home')
    template_name='parent_constituency_delete.html'
    
    def get_object(self, *args, **kwargs):
        obj = super(ParentConstituencyDeleteView, self).get_object(*args, **kwargs)
        if not obj.administrators.get(id = self.request.user.id).pk == self.request.user.id:
            raise Http404 # maybe you'll need to write a middleware to catch 403's same way
        return obj