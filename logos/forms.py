from django import forms
from models import Election

class ElectionForm(forms.ModelForm):
    
    class Meta:
        model = Election
        fields = ('constituency', 'name', 'description', 'first_voting_day', 'last_voting_day', 'moderators')