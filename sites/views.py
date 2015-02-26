from django.shortcuts import render
from sites.models import Site
from sites.models import Value
from django.http import Http404
from django.db.models import Sum, Avg
import itertools
import operator
    
def index(request):
    all_sites = Site.objects.all();
    return render(request, 'sites/index.html', {'all_sites':all_sites, 'title':'Sities'})
    

def detail(request, site_id):
    try:
        site = Site.objects.get(pk=site_id)
        values = site.value_set.all()
    except Site.DoesNotExist:
        raise Http404("Site does not exist")
    return render(request, 'sites/detail.html', {'values':values, 'site':site})

def accumulate(l):
    it = itertools.groupby(l, operator.itemgetter(0))
    list = []
    for key, subiter in it:
        sum_a, sum_b = [], []
        for n in subiter:
            sum_a.append(n[1])
            sum_b.append(n[2])
        list.append({'site__name':key, 'a_value':sum(sum_a), 'b_value':sum(sum_b)})
    return list

def summary(request):  
    v = Value.objects.values_list('site__name', 'a_value', 'b_value')
    values = list(accumulate(v))
#     values = Value.objects.values("site__name").annotate(a_value=Sum('a_value')).annotate(b_value =Sum('b_value'))
    return render(request, 'sites/summary.html', {'values':values, 'title':'Summary', 'aggre':'sum'})

def average(request):
    values = Value.objects.values("site__name").annotate(a_value=Avg('a_value')).annotate(b_value=Avg('b_value'))
    return render(request, 'sites/summary.html', {'values':values, 'title':'Summary', 'aggre':'avg'})
