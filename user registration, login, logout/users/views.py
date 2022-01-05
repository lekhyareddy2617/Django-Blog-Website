from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages #for alert messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username') #form.cleaned_data is a dictionary with validated form data
            messages.success(request,f'Account created with username {username}!')
            return redirect('login') #blog-home is name of url pattern of blog homepage
    else:
        form=UserRegisterForm()
    #if we get POST request, we have to validate the form data and if GET request, display the blank form
    return render(request,'users/register.html',{'form':form})

@login_required #decorators add functionality to function
def profile(request):
    return render(request,'users/profile.html')