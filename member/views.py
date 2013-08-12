from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.template import RequestContext
from member.forms import RegistrationForm, LoginForm
from member.models import Member
from django.contrib.auth import authenticate, login, logout


def MemberRegistration(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/my_account/')
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'], email=form.cleaned_data['email'],
                                            password=form.cleaned_data['password'])
            user.save()
            member = Member(user=user, first_name=form.cleaned_data['first_name'],
                            last_name=form.cleaned_data['last_name'], email=form.cleaned_data['email'],
                            birthday=form.cleaned_data['birthday'],
                            profile_picture=form.cleaned_data['profile_picture'])
            member.save()
            return HttpResponseRedirect('/my_account/')
        else:
            return render_to_response('register.html', {'form': form}, context_instance=RequestContext(request))

    else:
        '''user is not submitting the form, show them a blank registration form'''
        form = RegistrationForm()
        context = {'form': form}
        return render_to_response('register.html', context, context_instance=RequestContext(request))


def LoginRequest(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/my_account/')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            member = authenticate(username=username, password=password)
            if member is not None:
                login(request, member)
                return HttpResponseRedirect('/my_account/')
            else:
                return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))
        else:
            return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))
    else:
        ''' user is not submitting the form, show the login form '''
    form = LoginForm()
    return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))


def LogoutRequest(request):
    logout(request)
    return HttpResponseRedirect('/')


def show_my_account(request):
    return render_to_response("my_account.html", {}, context_instance=RequestContext(request))


def show_my_profiles(request):
    return render_to_response("my_profiles.html", {}, context_instance=RequestContext(request))