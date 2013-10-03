from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from everyvote_mini.models import ParentConstituency, Constituency, Office, Election, Candidate, UserProfile
from registration.forms import RegistrationFormUniqueEmail
from captcha.fields import ReCaptchaField

class RegistrationFormUniqueEmail(RegistrationFormUniqueEmail):
    captcha = ReCaptchaField()

class LoginForm(forms.Form):
    username = forms.CharField(label=u"User Name")
    password = forms.CharField(label=u'Password', widget=forms.PasswordInput(render_value=False))

class ParentConstituencyForm(forms.ModelForm):
    administrators = forms.ModelMultipleChoiceField(queryset=User.objects.order_by('username'))
    class Meta:
        model = ParentConstituency

class ParentConstituencyCreateForm(forms.ModelForm):
    class Meta:
        model = ParentConstituency
        exclude = ('administrators', )

class ConstituencyForm(forms.ModelForm):
    moderators = forms.ModelMultipleChoiceField(queryset=User.objects.order_by('username'))
    blocked_users = forms.ModelMultipleChoiceField(required=False, queryset=User.objects.order_by('username'))
    class Meta:
        model = Constituency

class ConstituencyCreateForm(forms.ModelForm):
    blocked_users = forms.ModelMultipleChoiceField(required=False, queryset=User.objects.order_by('username'))
    class Meta:
        model = Constituency
        exclude = ('moderators', )
        
class ElectionForm(forms.ModelForm):
    first_voting_day = forms.DateField(widget=forms.TextInput(attrs={ 'id':'datepicker_first_voting_day' }))
    last_voting_day = forms.DateField(widget=forms.TextInput(attrs={ 'id':'datepicker_last_voting_day' }))
    
    class Meta:
        model = Election
        exclude = ('is_featured', )

class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        exclude = ['user']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user', )        

# the moderator uses this along with CandidateCreateForm to create a user/candidate profile
# this uses the User model instead of UserProfile for the sake of simplicity for the moderator
class UserCreateForm(forms.ModelForm):
    
    class Meta:
        model = User
        exclude = ('last_login', 'date_joined', )
        
    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.set_password(self.cleaned_data["username"])
        if commit:
            user.save()
        return user

        
class OfficeForm(forms.ModelForm):
    class Meta:
        model = Office
        
class ContactForm(forms.Form):
    sender = forms.CharField(max_length=40)
    email = forms.EmailField()
    university = forms.CharField(max_length=60, required=False)
    message = forms.CharField(widget=forms.Textarea)
    captcha = ReCaptchaField()
