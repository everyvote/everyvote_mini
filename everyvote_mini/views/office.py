from everyvote_mini.models import Office
from everyvote_mini.forms import OfficeForm
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

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

# DELETE OFFICE
class OfficeDeleteView(DeleteView):
    model = Office
    success_url = reverse_lazy('home')
    template_name='office_delete.html'
