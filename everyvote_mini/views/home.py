from django.shortcuts import render_to_response
from everyvote_mini.models import ParentConstituency
from django.template import RequestContext


def home(request):
    return render_to_response('home.html',
                              {'parentconstituencies': ParentConstituency.objects.all()},
                              context_instance=RequestContext(request))