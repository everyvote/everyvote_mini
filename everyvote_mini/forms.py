from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from everyvote_mini.models import ParentConstituency, Constituency, Office, Election, Candidate, UserProfile

class LoginForm(forms.Form):
    username = forms.CharField(label=u"User Name")
    password = forms.CharField(label=u'Password', widget=forms.PasswordInput(render_value=False))

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user', )

class ParentConstituencyForm(forms.ModelForm):
    class Meta:
        model = ParentConstituency

class ConstituencyForm(forms.ModelForm):
    class Meta:
        model = Constituency

class ElectionForm(forms.ModelForm):
    class Meta:
        model = Election

class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        exclude = ['user']

class OfficeForm(forms.ModelForm):
    class Meta:
        model = Office
        
class ContactForm(forms.Form):
    email = forms.EmailField()
    university = forms.CharField()
    subject = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)