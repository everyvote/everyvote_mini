from django.contrib import admin
from logos.models import Constituency, Election, Office, Candidate
from member.models import Member

for model in [Constituency, Election, Office, Candidate, Member]:
    admin.site.register(model)