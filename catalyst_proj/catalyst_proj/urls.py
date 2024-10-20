"""
URL configuration for catalyst_proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from catalyst_app.views import login_view,manage_user_view,company_view,query_builder_view

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('catalyst_app/', include('catalyst_app.urls')),
    path('', login_view.user_login),
    path('login/', login_view.user_login, name='login'),
    path('register/', login_view.register_user, name='register'),
    path('logout', login_view.logout, name='logout'),
    path('manage_user/', manage_user_view.index, name='manage_user'),
    path('manage_user/add_user',manage_user_view.adduser,name='add_user'),
    path('manage_user/edituser', manage_user_view.edituser, name='edituser'),
    path('delete_user/', manage_user_view.delete_user, name='delete_user'),
    path('company/', company_view.index, name='company'),
    path('company/upload_company', company_view.upload_company_data, name='upload_company'),
    path('query_builder/', query_builder_view.index, name='query_builder'),
    path('api/filter_company/', query_builder_view.filter_company_data, name='filter_company'),


    
]
