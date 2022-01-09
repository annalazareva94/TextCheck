from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h4> lachibolala </h4>')

def resume(request):
    return render(request,'mainpage/resume.html')

def index(request):
    return render(request, 'mainpage/index.html')