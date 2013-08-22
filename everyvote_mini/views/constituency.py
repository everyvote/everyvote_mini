from everyvote_mini.models import Constituency
from everyvote_mini.forms import ConstituencyForm
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

"""
CONSTITUENCY
"""
# CREATE CONSTITUENCY
class ConstituencyCreateView(CreateView):
    model = Constituency
    form_class = ConstituencyForm
    template_name = 'constituency_create.html'
    
    def form_valid(self, form):
        f = form.save(commit=False)
        f.save()
        return super(ConstituencyCreateView, self).form_valid(form)


# LIST CONSTITUENCY
class ConstituencyListView(ListView):
    model = Constituency
    context_object_name = "constituencies"


# SHOW CONSTITUENCY
class ConstituencyDetailView(DetailView):
    model = Constituency
    context_object_name = "constituency"
        
    def get_context_data(self, **kwargs):
        context = super(ConstituencyDetailView, self).get_context_data(**kwargs)
        context['parent_constituency'] = self.get_object().parent_constituency
        return context
    
# UPDATE CONSTITUENCY
class ConstituencyUpdateView(UpdateView):
    model = Constituency
    form_class = ConstituencyForm
    template_name='constituency_form.html'


# DELETE CONSTITUENCY
class ConstituencyDeleteView(DeleteView):
    model = Constituency
    success_url = reverse_lazy('home')
    template_name='constituency_delete.html'