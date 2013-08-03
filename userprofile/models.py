from django.db import models
from django.contrib.auth.models import User
from time import time

def get_upload_file_name(instance, filename):
    return "uploaded_files/%s_%s" % (str(time()).replace('.','_'), filename)

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    likes_cheese = models.BooleanField()
    favourite_hamster_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    private_email = models.EmailField()
    profile_picture = models.FileField(upload_to=get_upload_file_name)
    
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])