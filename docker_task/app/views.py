from django.shortcuts import render
from django.http import HttpResponse

def return_msg(request):
    return HttpResponse("Hello, Docker!")


