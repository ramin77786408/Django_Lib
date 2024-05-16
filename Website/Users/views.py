from django.shortcuts import render, HttpResponseRedirect
from django.views import generic
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .forms import Signup

def sign_up(request):
    if request.method == 'POST':
        form = Signup(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return render(request,'registration/thanks.html')
            
    
    else:
        form = Signup()
    return render(request,'registration/signup.html', {'form': form})

    
