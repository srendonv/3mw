from django.shortcuts import render
from sites.models import Site
from sites.models import Value
from django.http import Http404
from django.db.models import Sum, Avg

def avg(list):

    sum = 0
    for elm in list:
        sum += elm

    sum/(len(list)*1.0)
    
def index(request):
    all_sites = Site.objects.all();
    return render(request,'sites/index.html',{'all_sites':all_sites,'title':'Sities'})
    

def detail(request, site_id):
    try:
        site = Site.objects.get(pk=site_id)
        values = site.value_set.all()
    except Site.DoesNotExist:
        raise Http404("Site does not exist")
    return render(request,'sites/detail.html',{'values':values,'site':site})

def summary(request):
    values = Value.objects.values("site__name").annotate(a_value=Sum('a_value')).annotate(b_value =Sum('b_value'))
    return render(request,'sites/summary.html',{'values':values,'title':'Summary','aggre':'sum'})

def average(request):
#     list = [3,4,1,20,102,3,5,67,39,28,10,1,4,34,1,6,107,99]
    values = Value.objects.values("site__name").annotate(a_value=Avg('a_value')).annotate(b_value =Avg('b_value'))

    return render(request,'sites/summary.html',{'values':values,'title':'Summary','aggre':'avg'})