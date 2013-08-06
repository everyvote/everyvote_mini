from django import forms
from models import Election, Candidate
from member.models import Member
from django.forms import ModelForm
from django.contrib.auth.models import User

class ElectionForm(forms.ModelForm):
    
    class Meta:
        model = Election
        fields = ('constituency', 'name', 'description', 'first_voting_day', 'last_voting_day')
        
"""class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('member', 'body')"""
        
class CandidateForm(forms.ModelForm):

    class Meta:
        model = Candidate

class ContactForm(forms.Form):
    email = forms.EmailField()
    university = forms.CharField()
    subject = forms.CharField()
    text = forms.CharField( widget=forms.Textarea )
