from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# A view function, or view for short, is a Python function that takes a web request and returns a web response. 
# This response can be the HTML contents of a web page, or a redirect, or a 404 error, or an XML document, or an image etc.

#posts=[
#    {
#       'author': 'Lekhya Reddy',
#        'title': 'Blog Post 1',
#        'content': 'First Post Content',
#        'date_posted': '23 August 2021'
#   },
#   {
#        'author': 'Shreya Patchala',
#        'title': 'Blog Post 2',
#        'content': 'Second Post Content',
#        'date_posted': '24 August 2021'
#    },
#   {
#        'author': 'Yash Laddha',
#        'title': 'Blog Post 3',
#        'content': 'Third Post Content',
#       'date_posted': '25 August 2021'
#    }
#]


def home(request):
    context={
        'posts':Post.objects.all()
    }
    return render(request,'blog/home.html',context)

class PostListView(ListView):
    model=Post
    template_name='blog/home.html'
    context_object_name='posts'
    ordering=['-date_posted']

class PostDetailView(DetailView):
    model=Post

class PostCreateView(LoginRequiredMixin,CreateView): #if we are not logged in and we want to create post (/post/new), we are first redirected to login page
    model=Post
    fields=['title','content']
    
    def form_valid(self,form):
        form.instance.author=self.request.user #setting author
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView): #LoginRequiredMixin: if we are not logged in and we want to create post (/post/new), we are first redirected to login page
    #UserPassesTestMixin: only author of post can update his/her post
    model=Post
    fields=['title','content']
    
    def form_valid(self,form):
        form.instance.author=self.request.user #setting author
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object() #we get the post we are currently trying to update
        if self.request.user==post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model=Post
    success_url='/'

    def test_func(self):
        post=self.get_object() #we get the post we are currently trying to update
        if self.request.user==post.author:
            return True
        return False

def about(request):
    return render(request,'blog/about.html',{'Title':'About'})
