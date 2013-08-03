from django import forms
from models import Election, Comment, Candidate

class ElectionForm(forms.ModelForm):
    
    class Meta:
        model = Election
        fields = ('constituency', 'name', 'description', 'first_voting_day', 'last_voting_day', 'moderators')

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('user', 'body')
        
class CandidateForm(forms.ModelForm):

    class Meta:
        model = Candidate