from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

from everyvote_mini.models import Constituency


def list(request):
    """ 
    This should list all the Constituencies.
    """
    
    return render_to_response('constituency/constituency_list.html',
        {'constituencies': Constituency.objects.all()},
        context_instance=RequestContext(request))