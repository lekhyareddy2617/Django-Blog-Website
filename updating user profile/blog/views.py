from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# A view function, or view for short, is a Python function that takes a web request and returns a web response. 
# This response can be the HTML contents of a web page, or a redirect, or a 404 error, or an XML document, or an image etc.

posts=[
    {
        'author': 'Lekhya Reddy',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': '23 August 2021'
    },
    {
        'author': 'Shreya Patchala',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': '24 August 2021'
    },
    {
        'author': 'Yash Laddha',
        'title': 'Blog Post 3',
        'content': 'Third Post Content',
        'date_posted': '25 August 2021'
    }
]


def home(request):
    context={
        'posts':Post.objects.all()
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'Title':'About'})
