from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.db import transaction
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.core.serializers import serialize
from django.template import loader
from django.db import models
from catalyst_app.models import company,Users
from django.urls import reverse
from django.db import connection,DataError
from datetime import datetime, timedelta ,date
from django.contrib.auth.hashers import make_password
from django.contrib import messages

def index(request):
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        user_data = Users.objects.all()
        # return HttpResponse(user_data)
        template = loader.get_template('manage_user.html')
        context = {
            'users_data' : user_data,
        }
        return HttpResponse(template.render(context,request))
    else:
        return HttpResponseRedirect('login') 

def adduser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        name = request.POST.get('name')
        password = request.POST.get('password')

        if Users.objects.filter(username=username).exists():
            return JsonResponse({"msg": "Username already exists."}, status=400)

        if username and name and password:
            hashed_password = make_password(password)
            # print(hashed_password)
            new_user = Users(
                username=username,
                name=name,
                password=hashed_password
            )
            new_user.save()
            return JsonResponse({"msg": "User added successfully!"}, status=200)

    return JsonResponse({"msg": "Failed to add user."}, status=400)



def edituser(request):
    if request.method == 'POST':
        userid = request.POST.get('edit_id', '')
        user_name = request.POST.get('edit_name', '')
        status = request.POST.get('edit_status', '')
        
        is_active = True if status == "1" else False
        user_update_count = Users.objects.filter(id=userid).update(name=user_name, is_active=is_active)

        if user_update_count > 0: 
            return JsonResponse({"msg": "User updated successfully!"}, status=200)
        else:
            return JsonResponse({"msg": "User not found or no changes made."}, status=404)

    return JsonResponse({"msg": "Invalid request method."}, status=400)
        

def delete_user(request):
    if request.method == 'POST':
        user_id = request.POST.get('id')
        user = get_object_or_404(Users, id=user_id)
        user.delete()
        return JsonResponse({"msg": "User deleted successfully!"}, status=200)
    return JsonResponse({"msg": "Failed to delete user."}, status=400)