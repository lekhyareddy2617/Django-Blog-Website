from django.shortcuts import render
from django.http import HttpResponse

# A view function, or view for short, is a Python function that takes a web request and returns a web response. 
# This response can be the HTML contents of a web page, or a redirect, or a 404 error, or an XML document, or an image etc.

def home(request):
    return HttpResponse('<h1>Blog Home</h1>')

def about(request):
    return HttpResponse('<h1>About</h1>')