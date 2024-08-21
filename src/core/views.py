from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisit



def home(request)->render:
    a = PageVisit.objects.create(path=request.path)
    print(a)
    query_set = PageVisit.objects.filter(path= request.path)
    print(query_set)
    context = {
        "page_visit_count": query_set.count()
    }
    print(request.path)
    return render(request, 'index.html', context)




def about(request):
    
    return render(request, 'index.html', context)
