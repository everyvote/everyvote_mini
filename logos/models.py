from django.db import models
from time import time

def get_upload_file_name(instance, filename):
    return "uploaded_files/%s_%s" % (str(time()).replace('.','_'), filename)

# Create your models here.


# class ParentConstituency(models.Model):
    # state_name = models.CharField(max_length=30)
    # city_name = models.CharField(max_length=30)
    
    # def __unicode__(self):
        # return self.state_name + ", " + city_name

        
class Constituency(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # image = ??? I dunno how to create image field yet
    # parentconstituency = models.ForeignKey(ParentConstituency)
    # administrators = models.ManyToManyField(User)
    
    def __unicode__(self):
        return self.name
        
        
class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    private_email = models.EmailField()
    profile_picture = models.FileField(upload_to=get_upload_file_name)
    # about_me = models.TextField()
    # public_email = models.EmailField()
    # twitter_name = models.CharField()
    # facebook_page = models.CharField()
    # linkedin_page = models.CharField()
    # personal_homepage = models.CharField()
    
    def __unicode__(self):
        return self.first_name + " " + self.last_name 
        
    
class Election(models.Model):
    constituency = models.ForeignKey(Constituency)
    name = models.CharField(max_length=50)
    description = models.TextField()
    first_voting_day = models.DateField()
    last_voting_day = models.DateField()
    moderators = models.ManyToManyField(User)
    # is this right? moderators = models.ManyToManyField()
    # is this right? blockusers = models.ManyToManyField()
        
    def __unicode__(self):
        return self.name

        
class Office(models.Model):
    election = models.ForeignKey(Election)
    name = models.CharField(max_length=30)
    description = models.TextField()
    # term_start = models.DateTimeField()
    # term_end = models.DateTimeField()

    def __unicode__(self):
        return self.name
        
        
class Candidate(models.Model):
    user = models.ForeignKey(User)
    election = models.ForeignKey(Election)
    office = models.ForeignKey(Office)
    description = models.TextField()
    # votes = models.ManyToManyField(User)
    
    def __unicode__(self):
        return unicode(self.user)
        
        
class Comment(models.Model):
    user = models.ForeignKey(User)
    body = models.TextField()
    created = models.DateTimeField()
    candidate = models.ForeignKey(Candidate)
    # how do we set up Comment table so user can comment on
    # moderators, administrators, and other users profiles?
    # moderator = models.ForeignKey(Moderator)
    # adminstrator = models.ForeignKey(Administrator)
    # user2 = how do we comment on another user's profile?

    def __unicode__(self):
        return self.body
    

# class Stance(models.Model):
    # name = models.TextField()
    # description = models.TextField()
    
    # def __unicode__(self):
        # return self.user


# class Vote(models.Model):
    # user = models.ForeignKey(User)
    # candidate = models.ForeignKey(Candidate)
    # stance = models.ForeignKey(Stance)
    # created = models.DateTimeField()
    
    # def __unicode__(self):
        # return self.user


