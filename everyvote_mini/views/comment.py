from django.contrib.comments.models import Comment
from django.http import Http404
from django.shortcuts import get_object_or_404
import django.contrib.comments.views.moderation as moderation
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType

def delete(request, comment_id):
    # g = Group.objects.get_or_create(name='Delete_Comment')
    # u = User.objects.get(username=request)
    # u.groups.add(g)
    # u.save()
    # group, created = Group.objects.get_or_create(name='Delete_Comment')
    # group.save()
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user == comment.user or \
       request.user.is_staff:
           return moderation.delete(request, comment_id)
    else:
        raise Http404