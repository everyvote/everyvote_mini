from everyvote_mini.models import Office
from everyvote_mini.forms import OfficeForm
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.http import Http404

"""
OFFICE
"""
# CREATE OFFICE
class OfficeCreateView(CreateView):
    model = Office
    form_class = OfficeForm
    template_name = 'office_create.html'
    
    def form_valid(self, form):
        f = form.save(commit=False)
        f.save()
        return super(OfficeCreateView, self).form_valid(form)

# SHOW OFFICE
class OfficeDetailView(DetailView):
    model = Office
    context_object_name = "office"
    
# UPDATE OFFICE
class OfficeUpdateView(UpdateView):
    model = Office
    form_class = OfficeForm
    template_name='office_form.html'
    
    def get_object(self, *args, **kwargs):
        obj = super(OfficeUpdateView, self).get_object(*args, **kwargs)
        if not obj.constituency.moderators.get(id = self.request.user.id).pk == self.request.user.id:
            raise Http404 # maybe you'll need to write a middleware to catch 403's same way
        return obj

# DELETE OFFICE
class OfficeDeleteView(DeleteView):
    model = Office
    success_url = reverse_lazy('home')
    template_name='office_delete.html'

    def get_object(self, *args, **kwargs):
        obj = super(OfficeDeleteView, self).get_object(*args, **kwargs)
        if not obj.constituency.moderators.get(id = self.request.user.id).pk == self.request.user.id:
            raise Http404 # maybe you'll need to write a middleware to catch 403's same way
        return obj