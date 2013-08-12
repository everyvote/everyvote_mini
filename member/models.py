from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from time import time


def get_upload_file_name(instance, filename):
    return "%s_%s" % (str(time()).replace('.', '_'), filename)


class Member(models.Model):
    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    birthday = models.DateField(null=True, blank=True)
    profile_picture = models.FileField(upload_to=get_upload_file_name)
    about_me = models.TextField(blank=True)
    public_email = models.EmailField(blank=True)
    twitter_name = models.URLField(blank=True)
    facebook_page = models.URLField(blank=True)
    linkedin_page = models.URLField(blank=True)
    personal_homepage = models.URLField(blank=True)

    def __unicode__(self):
        return self.first_name + " " + self.last_name

        # create our user object to attach to our member object
        # def create_member_user_callback(sender, instance, **kwargs):
        #    member, new = Member.objects.get_or_create(user=instance)
        # post_save.connect(create_member_user_callback, User)