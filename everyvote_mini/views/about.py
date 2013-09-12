from django.shortcuts import render_to_response
from django.template import RequestContext
from everyvote_mini.models import ParentConstituency

def about(request):
    return render_to_response('about.html',
                              {'parent_constituencies': ParentConstituency.objects.all()},
                              context_instance=RequestContext(request))