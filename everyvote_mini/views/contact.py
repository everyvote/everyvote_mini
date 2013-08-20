from django.shortcuts import render_to_response
from everyvote_mini.forms import ContactForm
from django.template import RequestContext
from django.core.mail import send_mail


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

            send_mail("Your subject", "Your text message! Data sent: %s %s %s %s" % (subject, university, text, email),
                      'bc789ok@gmail.com', ['mitchldowney@gmail.com'])
            # mail_admins("Your other subject", "Your other text")
    else:
        contact_form = ContactForm()

    ctx = {'contact_form': contact_form, 'email': email, 'subject': subject, 'university': university, 'text': text,
           'success': success}

    return render_to_response('contact.html', ctx, context_instance=RequestContext(request))
