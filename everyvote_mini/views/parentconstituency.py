from everyvote_mini.models import ParentConstituency
from django.views.generic import DetailView, ListView

"""
PARENT CONSTITUENCY
"""

# LIST PARENTCONSTITUENCY
class ParentConstituencyListView(ListView):
    model = ParentConstituency

# SHOW PARENTCONSTITUENCY
class ParentConstituencyDetailView(DetailView):
    model = ParentConstituency
    context_object_name = "parentconstituency"