from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

# def register_request(request):
#     # return render(request, "register.html", {"register_form" : NewUserForm()})

def register_request(request):
	if request.method == "POST":
		print(request.POST)
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect("register")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data = request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password  = form.cleaned_data.get('password')
			user = authenticate(username = username, password = password)
			if user:
				login(request, user)
				return redirect("home_page")
			else:
				pass
		else:
			pass
	form = AuthenticationForm()
	return render(request,  "login.html", {"login_form" : form})


def logout_request(request):
	logout(request)
	return redirect("login_user")
			