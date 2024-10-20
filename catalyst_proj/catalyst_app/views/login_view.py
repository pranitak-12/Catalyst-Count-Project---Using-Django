from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.contrib.auth import authenticate
from django.core.serializers import serialize
from django.template import loader
from django.db import models
from django.db.models import Count, Q
from catalyst_app.models import Users
from django.urls import reverse
from django import forms 
from django.db import connection,DataError
from datetime import datetime, timedelta ,date
from django.contrib.auth.hashers import make_password, check_password
import json,csv
from django.contrib import messages

from django.contrib.auth import login as auth_login 
from django.contrib.auth import logout as auth_logout

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        if not username or not password:
            messages.error(request, "Username and password cannot be empty.")
            return redirect('login')

        try:
            user = Users.objects.get(username=username)
            if user.check_password(password):
                if user.is_active:
                    auth_login(request, user)
                    request.session['user_id'] = user.id
                    request.session['username'] = user.username
                    request.session['name'] = user.name
                    return redirect('company')  
                else:
                    messages.error(request, "User account is inactive.")
            else:
                messages.error(request, "Invalid username or password.")
        except Users.DoesNotExist:
            messages.error(request, "Invalid username or password.")

        return redirect('login')
    else:
        return render(request, 'login.html') 


def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        name = request.POST.get('name', '').strip()
        password = request.POST.get('password', '').strip()
        confirm_password = request.POST.get('confirm_password', '').strip()

        # Validate input fields
        if not username or not name or not password or not confirm_password:
            messages.error(request, "All fields are required.")
            return redirect('register')  

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('register')  

        try:
            # Create a new user instance
            user = Users(username=username, name=name)
            user.set_password(password)  
            user.save()  

            messages.success(request, "Registration successful. You can now log in.")
            return redirect('login') 

        except IntegrityError:
            messages.error(request, "Username already exists.")
            return redirect('register')  
    else:
        return render(request, 'register.html') 


def logout(request):
    auth_logout(request) 
    return redirect('login')