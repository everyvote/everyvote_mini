from everyvote_mini.models import UserProfile
from everyvote_mini.forms import UserProfileForm
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model


# SHOW USERPROFILE
class UserProfileDetailView(DetailView):
    model = get_user_model()
    slug_field = 'username'
    template_name = "user_detail.html"
    
    def get_object(self, queryset=None):
        user = super(UserProfileDetailView, self).get_object(queryset)
        UserProfile.objects.get_or_create(user=user)
        return user

# UPDATE USERPROFILE
class UserProfileUpdateView(UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = "user_form.html"
        
    def get_object(self, queryset=None):
        return UserProfile.objects.get_or_create(user=self.request.user)[0]
    
    def get_success_url(self):
        return reverse('user_detail', kwargs={'slug': self.request.user})