from django.contrib import admin
from logos.models import Constituency, User, Election, Office, Candidate, Comment
from userprofile.models import UserProfile

for model in [Constituency, User, Election, Office, Candidate, Comment, UserProfile],:
    admin.site.register(model)