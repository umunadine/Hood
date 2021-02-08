from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
import datetime as dt
from .models import Neighborhood, Profile, Business, Alert, Hospital
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from .forms import RegisterForm, NewBusinessForm, ProfileUpdateForm, NewAlertForm
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            user = User.objects.get(username=username)
            profile=Profile.objects.create(user=user,email=email)
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request,'registration/registration_form.html')

@login_required
def index(request):
    hoods = Neighborhood.objects.all()
    return render(request,'index.html',{'hoods':hoods})
    
