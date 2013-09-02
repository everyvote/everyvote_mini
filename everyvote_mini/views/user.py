from everyvote_mini.models import UserProfile
from everyvote_mini.forms import UserProfileForm
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse, reverse_lazy
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
    model = get_user_model()
    form_class = UserProfileForm
    slug_field = 'username'
    template_name = "user_form.html"

    def get_success_url(self):
        return reverse('user_detail', kwargs={'slug': self.request.user})
        
    def get_object(self, *args, **kwargs):
        user = super(UserProfileUpdateView, self).get_object(*args, **kwargs)
        if not user.id == self.request.user.id:
            raise Http404 # maybe you'll need to write a middleware to catch 403's same way
        return user
