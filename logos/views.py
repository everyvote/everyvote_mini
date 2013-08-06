from django.shortcuts import render_to_response
from logos.models import Constituency, Election, Office, Candidate
from member.models import Member
from django.http import HttpResponse
from forms import ElectionForm, CandidateForm, ContactForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.utils import timezone
from django.template import RequestContext
from django.core.mail import send_mail
# Create your views here.

def show_base(request):
    return render_to_response("base.html", {}, context_instance=RequestContext(request))

def constituencies(request):
    return render_to_response('constituencies.html',
                             {'constituencies': Constituency.objects.all() },
                             context_instance=RequestContext(request))

def constituency(request, constituency_id=1):
    return render_to_response('constituency.html',
                             {'constituency': Constituency.objects.get(id=constituency_id) },
                             context_instance=RequestContext(request))

def candidates(request):
    return render_to_response('candidates.html',
                             {'candidates': Candidate.objects.all() },
                             context_instance=RequestContext(request))

def candidate(request, candidate_id=1):
    return render_to_response('candidate.html',
                             {'candidate': Candidate.objects.get(id=candidate_id) },
                             context_instance=RequestContext(request))

def elections(request):
    return render_to_response('elections.html',
                             {'elections': Election.objects.all() },
                             context_instance=RequestContext(request))

def election(request, election_id=1):
    return render_to_response('election.html',
                             {'election': Election.objects.get(id=election_id) },
                             context_instance=RequestContext(request))
                             
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
    
    return render_to_response('add_election.html', args, context_instance=RequestContext(request))

def add_candidate(request):
    if request.POST:
        form = CandidateForm(request.POST)
        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect('/candidates/all')
    else:
        form = CandidateForm()
        
    args = {}
    args.update(csrf(request))
    
    args['form'] = form
    
    return render_to_response('add_candidate.html', args, context_instance=RequestContext(request))

def add_comment(request, candidate_id):
    a = Candidate.objects.get(id=candidate_id)
    
    if request.method == "POST":
        f = CommentForm(request.POST)
        if f.is_valid():
            c = f.save(commit=False)
            c.created = timezone.now()
            c.candidate = a
            c.save()
            
            return HttpResponseRedirect('/candidates/get/%s' % candidate_id)
            
    else:
        f = CommentForm()
        
    args = {}
    args.update(csrf(request))
    
    args['candidate'] = a
    args['form'] = f
    
    return render_to_response('add_comment.html', args, context_instance=RequestContext(request))
    
def contact(request):

    success = False
    email = ""
    university = ""
    subject = ""
    text = ""

    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        
        if contact_form.is_valid():
            success = True
            email = contact_form.cleaned_data['email']
            subject = contact_form.cleaned_data['subject']
            university = contact_form.cleaned_data['university']
            text = contact_form.cleaned_data['text']
            
            send_mail("Your subject", "Your text message! Data sent: %s %s %s" % (title,university,text,email), 'mail.from@server.com', ['user.to@server.com'])
            # mail_admins("Your other subject", "Your other text")
    else:
        contact_form = ContactForm()
        
    ctx = {'contact_form':contact_form, 'email':email, 'subject':subject, 'university':university, 'text':text, 'success':success}
    
    return render_to_response('contact.html', ctx, context_instance=RequestContext(request))