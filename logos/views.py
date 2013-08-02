from django.shortcuts import render_to_response
from logos.models import Constituency, Candidate, Election
from django.http import HttpResponse
from forms import ElectionForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf

# Create your views here.

def show_base(request):
    return render_to_response('base.html')

def constituencies(request):
    return render_to_response('constituencies.html',
                             {'constituencies': Constituency.objects.all() })

def constituency(request, constituency_id=1):
    return render_to_response('constituency.html',
                             {'constituency': Constituency.objects.get(id=constituency_id) })

def candidates(request):
    return render_to_response('candidates.html',
                             {'candidates': Candidate.objects.all() })

def candidate(request, candidate_id=1):
    return render_to_response('candidate.html',
                             {'candidate': Candidate.objects.get(id=candidate_id) })

def elections(request):
    return render_to_response('elections.html',
                             {'elections': Election.objects.all() })

def election(request, election_id=1):
    return render_to_response('election.html',
                             {'election': Election.objects.get(id=election_id) })
                             
def add_election(request):
    if request.POST:
        form = ElectionForm(request.POST)
        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect('/elections/all')
    else:
        form = ElectionForm()
        
    args = {}
    args.update(csrf(request))
    
    args['form'] = form
    
    return render_to_response('add_election.html', args)