from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from everyvote_mini.forms import ContactForm
from django.template import RequestContext
from django.core.mail import send_mail
from everyvote_mini.models import ParentConstituency

def contact(request):
    success = False
    sender = ""
    email = ""
    university = ""
    message = ""

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            success = True
            sender = form.cleaned_data['sender']
            email = form.cleaned_data['email']
            university = form.cleaned_data['university']
            message = form.cleaned_data.get('message')

            recipients = ['contactus@everyvote.org']
            
            send_mail('Contact EV', 'Email: %s - University: %s - Message: %s' % (email, university, message), sender, recipients)
            return HttpResponseRedirect('/thanks/')

    else:
        form = ContactForm()
    
    ctx = {'form':form, 'sender':sender, 'email':email, 'university':university, 'message':message, 'success':success}
    
    return render_to_response('contact.html', ctx, context_instance=RequestContext(request))
    
def thanks(request):
    return render_to_response('thanks.html',
                              {'parent_constituencies': ParentConstituency.objects.all()},
                              context_instance=RequestContext(request))