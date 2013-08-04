from django.contrib import admin
from logos.models import Constituency, User, Election, Office, Candidate, Comment
from member.models import Member

for model in [Constituency, User, Election, Office, Candidate, Comment, Member]:
    admin.site.register(model)