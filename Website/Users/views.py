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
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username, email=email,
                                            first_name=first_name,last_name=last_name, password=password)
            user.save()
            return render(request,'registration/thanks.html')
            
    
    else:
        form = Signup()
    return render(request,'registration/signup.html', {'form': form})

    
