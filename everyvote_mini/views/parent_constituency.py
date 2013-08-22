from everyvote_mini.models import ParentConstituency
from django.views.generic import DetailView, ListView

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