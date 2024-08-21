from django.http import HttpResponse
from django.shortcuts import render



def home(request)->render:
    # context = {
    #     "item1": 'hello world',
    # }
    return render(request, 'index.html')




def about(request):
    return
