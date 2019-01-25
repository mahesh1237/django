from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
    return HttpResponse("welcome to student project")
def addstudent(request):
    return HttpResponse('student registration')
def addemployee(request):
    return HttpResponse('employee registration')

