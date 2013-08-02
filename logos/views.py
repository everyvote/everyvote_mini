from django.shortcuts import render_to_response
from logos.models import Constituency, Candidate, Election
from django.http import HttpResponse

# Create your views here.

def language(request, language='en-us'):
    response = HttpResponse("setting language to %s" % language)
    
    response.set_cookie('lang', language)
    
    request.session['lang'] = language
    
    return response

def constituencies(request):
    language = 'en-us'
    session_language = 'en-gb'
    
    if 'lang' in request.COOKIES:
        language = request.COOKIES['lang']
    
    if 'lang' in request.session:
        session_language = request.session['lang']
    
    return render_to_response('constituencies.html',
                             {'constituencies': Constituency.objects.all(),
                             'language' : language,
                             'session_language' : session_language})

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