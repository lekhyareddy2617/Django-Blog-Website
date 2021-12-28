from django.shortcuts import render
from django.http import HttpResponse

# A view function, or view for short, is a Python function that takes a web request and returns a web response. 
# This response can be the HTML contents of a web page, or a redirect, or a 404 error, or an XML document, or an image etc.

posts=[
    {
        'Author': 'Lekhya Reddy',
        'Title': 'Blog Post 1',
        'Content': 'First Post Content',
        'DateOfPosting': '23 August 2021'
    },
    {
        'Author': 'Shreya Patchala',
        'Title': 'Blog Post 2',
        'Content': 'Second Post Content',
        'DateOfPosting': '24 August 2021'
    },
    {
        'Author': 'Yash Laddha',
        'Title': 'Blog Post 3',
        'Content': 'Third Post Content',
        'DateOfPosting': '25 August 2021'
    }
]


def home(request):
    context={
        'posts':posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'Title':'About'})
