from django.shortcuts import render, redirect 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout
from .models import room, switchboard

# Create your views here.


def home(request):
	return render(request, 'webapp/home.html')

def signupuser(request):
	if request.method == 'GET':
		return render(request, 'webapp/signupuser.html', {'form' : UserCreationForm()})
	else: 
		#creating New User
		if request.POST['password1'] == request.POST['password2']:
			try:
				user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
				user.save()
				login(request, user)
				return redirect("test_esp_led")
			except IntegrityError:
				return render(request, 'webapp/signupuser.html', {'form' : UserCreationForm(), 'error':'That username is already taken, Please take another! '}) 



		else:
			#print('hello')
			#tell user that pasword isnt matching 
			return render(request, 'webapp/signupuser.html', {'form' : UserCreationForm(), 'error':'Please check the password again'})


def after_login(request):
	return render(request, 'webapp/after_login.html')


def logoutuser(request):
	if request.method == 'POST':
		logout(request)
	return redirect(home)



def Display_info(request):
	esp_room_info = room.objects.all()
	esp_ip_address = switchboard.objects.all()
	return render(request, 'webapp/test_html.html', {'room_info':esp_room_info, 'ress': esp_ip_address})