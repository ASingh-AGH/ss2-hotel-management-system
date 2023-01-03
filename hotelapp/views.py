from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.urls import reverse
from urllib.parse import urlencode
from .forms import UserRegistrationForm
from .models import Rooms

def home(request):
    room=Rooms.objects.all()
    return render(request, 'hotelapp/home.html', {'room':room})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'hotelapp/register.html', context)

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("home")

def room_info(request):
    return render(request, 'hotelapp/roomInfo.html')