from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisit



def home(request)->render:
    PageVisit.objects.create(path=request.path)
    query_set = PageVisit.objects.filter(path= request.path)
    qs = PageVisit.objects.filter()
    try:
        percent = query_set.count()*100 / qs.count()
    except:
        percent = 0
    context = {
        "page_visit_count": query_set.count(),
        "percent": percent,
    }
    print(request.path)
    return render(request, 'index.html', context)




def about(request):
    
    PageVisit.objects.create(path=request.path)
    query_set = PageVisit.objects.filter(path= request.path)
    qs = PageVisit.objects.filter()
    try:
        percent = query_set.count()*100 / qs.count()
    except:
        percent = 0
    context = {
        "page_visit_count": query_set.count(),
        "percent": percent,
    }
    print(request.path)
    return render(request, 'index.html', context)
