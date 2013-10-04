from django.shortcuts import render_to_response
from everyvote_mini.models import ParentConstituency, Election
from django.template import RequestContext


def home(request):
    return render_to_response('home.html',
                              {'parent_constituencies': ParentConstituency.objects.all(),
                               'featured_elections': Election.objects.filter(is_featured=True).order_by('?')},
                              context_instance=RequestContext(request))