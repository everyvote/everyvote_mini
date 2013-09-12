from everyvote_mini.models import Constituency
from everyvote_mini.forms import ConstituencyForm, ConstituencyCreateForm
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

"""
CONSTITUENCY
"""
# CREATE CONSTITUENCY
class ConstituencyCreateView(CreateView):
    model = Constituency
    form_class = ConstituencyCreateForm
    template_name = 'constituency_create.html'
    
    def form_valid(self, form):
        f = form.save(commit=False)
        f.save()
        f.moderators.add(self.request.user)
        form.save_m2m()
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

    def get_object(self, *args, **kwargs):
        obj = super(ConstituencyUpdateView, self).get_object(*args, **kwargs)
        if not obj.moderators.get(id = self.request.user.id).pk == self.request.user.id:
            raise Http404 # maybe you'll need to write a middleware to catch 403's same way
        return obj

# DELETE CONSTITUENCY
class ConstituencyDeleteView(DeleteView):
    model = Constituency
    success_url = reverse_lazy('home')
    template_name='constituency_delete.html'
    
    def get_object(self, *args, **kwargs):
        obj = super(ConstituencyDeleteView, self).get_object(*args, **kwargs)
        if not obj.moderators.get(id = self.request.user.id).pk == self.request.user.id:
            raise Http404 # maybe you'll need to write a middleware to catch 403's same way
        return obj
