from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def M(request):
    return HttpResponse("M App")