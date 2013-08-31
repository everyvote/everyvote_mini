from django.shortcuts import render_to_response
from django.template import RequestContext
from everyvote_mini.models import ParentConstituency

def about(request):
    return render_to_response('about.html',
                              {'parent_constituencies': ParentConstituency.objects.all()},
<<<<<<< HEAD
                              context_instance=RequestContext(request))
=======
                              context_instance=RequestContext(request))
>>>>>>> 3238077c484161004301f852c2631ea0cb6e2fcb
