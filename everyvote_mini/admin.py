from django.contrib import admin
from everyvote_mini.models import ParentConstituency, Constituency, Election, Office, Candidate, UserProfile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

for model in [ParentConstituency, Constituency, Election, Office, Candidate]:
    admin.site.register(model)

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    
class UserProfileAdmin(UserAdmin):
    inlines=(UserProfileInline, )
    
admin.site.unregister(get_user_model())
admin.site.register(get_user_model(), UserProfileAdmin)