from django.db import models
from django.contrib.auth.models import User, Group
from time import time
from django.core.urlresolvers import reverse
from django_resized import ResizedImageField

# This doesn't belong here
def get_upload_file_name(instance, filename):
    return "%s_%s" % (str(time()).replace('.', '_'), filename)

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
    about = models.TextField(blank=True)
    administrators = models.ManyToManyField(User, blank=True)
    profile_picture = ResizedImageField(upload_to=get_upload_file_name, blank=True, max_width=250, max_height=250)
    email = models.EmailField(blank=True)
    twitter_name = models.CharField(max_length=20, blank=True)
    facebook_page = models.URLField(blank=True)
    linkedin_page = models.URLField(blank=True)
    personal_homepage = models.URLField(blank=True)
    
    class Meta:
        ordering = ['name']
    
    def __unicode__(self):
        return unicode(self.name)

    def get_absolute_url(self):
        return reverse('parent_constituency_detail', kwargs={'pk': str(self.id)})

class Constituency(models.Model):
    parent_constituency = models.ForeignKey(ParentConstituency)
    name = models.CharField(max_length=100)
    about = models.TextField(blank=True)
    moderators = models.ManyToManyField(User, related_name='moderator')
    blocked_users = models.ManyToManyField(User, related_name='blocked_users', blank=True, null=True)
    profile_picture = ResizedImageField(upload_to=get_upload_file_name, blank=True, max_width=250, max_height=250)
    email = models.EmailField(blank=True)
    twitter_name = models.CharField(max_length=20, blank=True)
    facebook_page = models.URLField(blank=True)
    linkedin_page = models.URLField(blank=True)
    personal_homepage = models.URLField(blank=True)
    
    class Meta:
        ordering = ['parent_constituency']
    
    class Meta:
        ordering = ['name']
    
    def __unicode__(self):
        return u'%s - %s' % (self.parent_constituency.name, self.name)
        
    def get_absolute_url(self):
        return reverse('constituency_detail', kwargs={'pk': str(self.id)})

class Office(models.Model):
    constituency = models.ForeignKey(Constituency)
    name = models.CharField(max_length=30)
    about = models.TextField(blank=True)

    class Meta:
        ordering = ['constituency']
    
    def __unicode__(self):
        return u'%s - %s - %s' % (self.constituency.parent_constituency.name, self.constituency.name, self.name)

    def get_absolute_url(self):
        return reverse('office_detail', kwargs={'pk': str(self.id)})

class Election(models.Model):
    constituency = models.ForeignKey(Constituency)
    name = models.CharField(max_length=50)
    about = models.TextField(blank=True)
    first_voting_day = models.DateField()
    last_voting_day = models.DateField(blank=True, null=True)
    offices = models.ManyToManyField(Office, blank=True, null=True)
    """ Research: Django's Auth provides some sort of 
        access control. How/Can we use that? """

    class Meta:
        ordering = ['name']

    def get_office_candidates(self, office_id):
        office_candidates = self.candidate_set.filter(office_id=office_id)
        
        return office_candidates

    def moderator_candidate_queue(self):
        moderator_candidate_queue = self.candidate_set.filter(is_approved__isnull=True)
        print moderator_candidate_queue
        
        return moderator_candidate_queue

    def eligible_candidates(self):
        
        blocked_users = self.constituency.blocked_users.all()
        print blocked_users
        
        eligible_candidates = self.candidate_set.filter(is_approved=True).exclude(user__in = blocked_users)
        
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
    profile_picture = ResizedImageField(upload_to=get_upload_file_name, blank=True, max_width=250, max_height=250)
    about = models.TextField(blank=True)
    party = models.CharField(max_length=50, blank=True)
    year_in_school = models.CharField(max_length=25, blank=True)
    major = models.CharField(max_length=75, blank=True)
    twitter_name = models.CharField(max_length=20, blank=True)
    facebook_page = models.URLField(blank=True)
    linkedin_page = models.URLField(blank=True)
    personal_homepage = models.URLField(blank=True)
    
    class Meta:
        ordering = ['user']
    
    def __unicode__(self):
        return unicode(self.user)


class Candidate(models.Model):
    user = models.ForeignKey(UserProfile)
    election = models.ForeignKey(Election)
    office = models.ForeignKey(Office)
    party = models.CharField(max_length=50, blank=True)
    goals = models.TextField(blank=True)
    experience = models.TextField(blank=True)
    about = models.TextField(blank=True)
    is_approved = models.NullBooleanField()
    
    class Meta:
        ordering = ['?']
        
    def __unicode__(self):
        return u'%s %s for %s in the %s' % (self.user.first_name, self.user.last_name, self.office.name, self.election)

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


class Stance(models.Model):
    name = models.TextField()
    about = models.TextField()

    
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
