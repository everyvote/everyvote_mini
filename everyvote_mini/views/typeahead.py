from everyvote_mini.models import ParentConstituency, Constituency
from django.http import HttpResponse
from django.utils.html import escape
from django.utils import simplejson

# TYPEAHEAD PARENT CONSTITUENCY
def typeahead(request, search_type):
    resultSet = {}
    if search_type == 'universities':
        if request.method == "GET":
            if request.GET.has_key(u'query'):
                query = request.GET[u'query']
                obj = ParentConstituency.objects.filter(name__contains=query)
                results = [ ]
                for x in obj:
                   results.append({'value':'%s' % x.name,
                   'tokens':x.name.split() + ['%s' % x.id,],
                   'name':x.name,
                   'number':x.id})
                resultSet["options"] = results
        json = simplejson.dumps(results)
    return HttpResponse(json, content_type="application/json")
                   
"""
# TYPEAHEAD PARENT CONSTITUENCY
def typeahead(request, search_type):
    resultSet = {}
    if search_type == 'universities':
        if request.method == "GET":
            if request.GET.has_key(u'query'):
                query = request.GET[u'query']
                obj = ParentConstituency.objects.filter(name__contains=query)
                results = [ x.name for x in obj ]
                resultSet["options"] = results
        json = simplejson.dumps(resultSet)
    return HttpResponse(json, content_type="application/json")
"""