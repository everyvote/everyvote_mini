from django.db import models
from django.contrib.auth.models import User, Group
from time import time
from django.core.urlresolvers import reverse

# This doesn't belong here
def get_upload_file_name(instance, filename):
    return "uploaded_files/%s_%s" % (str(time()).replace('.', '_'), filename)

# ParentConstituency
# Constituency
# Office
# Election
# UserProfile
# Candidate
# Stance
# Vote


class ParentConstituency(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    administrators = models.ManyToManyField(User)
    
    def __unicode__(self):
        return unicode(self.name)


class Constituency(models.Model):
    parent_constituency = models.ForeignKey(ParentConstituency)
    name = models.CharField(max_length=100)
    description = models.TextField()
    moderators = models.ManyToManyField(User, related_name='moderator')
    blocked_users = models.ManyToManyField(User, related_name='blocked_users', blank=True)
    
    def __unicode__(self):
        return u'%s - %s' % (self.parent_constituency.name, self.name)
        
    def get_absolute_url(self):
        return reverse('parent_constituency_detail', kwargs={'pk': str(self.id)})


class Office(models.Model):
    constituency = models.ForeignKey(Constituency)
    name = models.CharField(max_length=30)
    description = models.TextField()

    def __unicode__(self):
        return u'%s - %s - %s' % (self.constituency.parent_constituency.name, self.constituency.name, self.name)


class Election(models.Model):
    constituency = models.ForeignKey(Constituency)
    name = models.CharField(max_length=50)
    description = models.TextField()
    first_voting_day = models.DateField()
    last_voting_day = models.DateField(null=True, blank=True)
    offices = models.ManyToManyField(Office)
    """ Research: Django's Auth provides some sort of 
        access control. How/Can we use that? """
    
    def eligible_candidates(self):
        
        blocked_users = self.blocked_users.all()
        print blocked_users
        
        eligible_candidates = self.candidate_set.exclude(
            user__in = blocked_users)
        
        print eligible_candidates
            
        return eligible_candidates   

    def get_absolute_url(self):
        return reverse('election_detail', kwargs={'pk': str(self.id)})

    def __unicode__(self):
        return u'%s - %s - %s' % (self.constituency.parent_constituency.name, self.constituency.name, self.name)

class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    profile_picture = models.FileField(upload_to=get_upload_file_name, blank=True)
    about_me = models.TextField(blank=True)
    twitter_name = models.CharField(max_length=20, blank=True)
    facebook_page = models.URLField(blank=True)
    linkedin_page = models.URLField(blank=True)
    personal_homepage = models.URLField(blank=True)
    
    def __unicode__(self):
        return unicode(self.user)


class Candidate(models.Model):
    user = models.ForeignKey(UserProfile)
    election = models.ForeignKey(Election)
    office = models.ForeignKey(Office)
    description = models.TextField()

    
    class Meta:
        ordering = ['?']
    
    def __unicode__(self):
        return unicode(self.user)

    def get_absolute_url(self):
        return reverse('candidate_detail', kwargs={'pk': str(self.id)})

# i don't really understand what this is, what it does, why it's not indented, and if we need it for other stuff too --mitch
# It looks like this code configures django so that it creates a profile whenever a user is created-- it seems pretty out of place though. -vince
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = UserProfile.objects.get_or_create(user=instance)
        """putting this here will screw up syncdb, because the 'Delete_Comment' group is not yet created
        i tried defining a function to create an auth group named 'Delete_Comment' but every time i tried
        to do the initial syncdb, it would return "DatabaseError: no such table: auth_group"...buuuut
        here's a gross way to make delete commments work for demo purposes: you can run syncdb with the 
        following 4 lines commented out, then add the Delete_Comment group through Django's admin panel, and set 
        the user permissions to "can moderate comment." All new registered users will then automatically have 
        the permission needed to delete their own comment"""
        # g = Group.objects.get(name='Delete_Comment')
        # u = User.objects.get(username=instance)
        # u.groups.add(g)
        # u.save()

from django.db.models.signals import post_save
post_save.connect(create_profile, sender=User)

"""
class Comment(models.Model):
    user = models.ForeignKey(User)
    body = models.TextField()
    created = models.DateTimeField(time)
    candidate = models.ForeignKey(Candidate)

    def __unicode__(self):
        return unicode(self.user)
"""

class Stance(models.Model):
    name = models.TextField()
    description = models.TextField()

    
class Vote(models.Model):
    UPVOTE = '1'
    DOWNVOTE = '2'

    user = models.ForeignKey(User)
    candidate = models.ForeignKey(Candidate)
    stance = (
        (UPVOTE, 'Upvote'),
        (DOWNVOTE, 'Downvote')
    )
    created = models.DateTimeField()

    def __unicode__(self):
        return "Vote by: " + str(self.user)