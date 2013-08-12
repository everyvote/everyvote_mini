from django.db import models
from django.contrib.auth.models import User
from member.models import Member
from time import time


# This doesn't belong here
def get_upload_file_name(instance, filename):
    return "uploaded_files/%s_%s" % (str(time()).replace('.', '_'), filename)

# class ParentConstituency(models.Model):
# state_name = models.CharField(max_length=30)
# city_name = models.CharField(max_length=30)

# def __unicode__(self):
# return self.state_name + ", " + city_name


class Constituency(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # parentconstituency = models.ForeignKey(ParentConstituency)
    administrators = models.ManyToManyField(Member)

    def __unicode__(self):
        return self.name


class Office(models.Model):
    constituency = models.ForeignKey(Constituency)
    name = models.CharField(max_length=30)
    description = models.TextField()

    def __unicode__(self):
        return "%s at %s" % (self.name, self.constituency)


class Election(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    first_voting_day = models.DateField()
    last_voting_day = models.DateField()
    constituency = models.ForeignKey(Constituency)
    offices = models.ManyToManyField(Office)

    """ Research: Django's Auth provides some sort of 
        access control. How/Can we use that? """
    moderators = models.ManyToManyField(Member, related_name='moderator')
    blocked_users = models.ManyToManyField(Member, related_name='blocked_users', blank=True)

    def __unicode__(self):
        return "%s election at %s" % (self.name, self.constituency)


class Candidate(models.Model):
    # Relations
    member = models.ForeignKey(Member)
    office = models.ForeignKey(Office)
    election = models.ForeignKey(Election)

    # Properties
    description = models.TextField()

    def __unicode__(self):
        return "%s running for %s of %s at %s" % (self.member, self.office.name, self.election.name, self.election.constituency.name)


class Stance(models.Model):
    name = models.TextField()
    description = models.TextField()

    # def __unicode__(self):
    # return self.member


class Vote(models.Model):
    UPVOTE = '1'
    DOWNVOTE = '2'

    member = models.ForeignKey(Member)
    candidate = models.ForeignKey(Candidate)
    stance = (
        (UPVOTE, 'Upvote'),
        (DOWNVOTE, 'Downvote')
    )
    created = models.DateTimeField()

    def __unicode__(self):
        return "Vote by: " + str(self.member)
