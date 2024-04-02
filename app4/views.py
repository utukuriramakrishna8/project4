from django.shortcuts import render
from django.http import HttpResponse

def string(request):
    return HttpResponse('String Response')
def styles(request):
    return render(request,'ram.html') 
