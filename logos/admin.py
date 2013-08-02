from django.contrib import admin
from logos.models import Constituency, User, Election, Office, Candidate, Comment

for model in [Constituency, User, Election, Office, Candidate, Comment]:
    admin.site.register(model)