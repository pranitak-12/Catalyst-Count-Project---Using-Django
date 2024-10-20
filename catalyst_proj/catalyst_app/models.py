from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.hashers import make_password, check_password as check_user_password

class UsersManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

class Users(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True, db_column='username')
    name = models.CharField(max_length=100, db_column='name')
    password = models.CharField(max_length=128, db_column='password')
    is_active = models.BooleanField(default=True) 
    is_staff = models.BooleanField(default=False) 

    objects = UsersManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name'] 

    class Meta:
        db_table = 'users'
        ordering = ('-id',)

    def check_password(self, raw_password):
        return check_user_password(raw_password, self.password)


class company(models.Model):
  company_id = models.IntegerField(null=True,blank=True,db_column='company_id',default=None)
  name = models.CharField(max_length=100,null=True,blank=True,db_column='name')
  domain = models.CharField(max_length=200,null=True,blank=True,db_column='domain')
  year_founded = models.IntegerField(null=True,blank=True,db_column='year_founded')
  industry = models.CharField(max_length=200,null=True,blank=True,db_column='industry')
  size_range = models.CharField(max_length=200,null=True,blank=True,db_column='size_range')
  locality = models.CharField(max_length=500,null=True,blank=True,db_column='locality')
  country = models.CharField(max_length=100,null=True,blank=True,db_column='country')
  linkedin_url = models.CharField(max_length=500,null=True,blank=True,db_column='linkedin_url')
  current_emp_est = models.IntegerField(null=True,blank=True,db_column='current_emp_est')
  total_emp_est = models.IntegerField(null=True,blank=True,db_column='total_emp_est')
  userid = models.ForeignKey(Users,null=True,on_delete=models.DO_NOTHING, db_column="userid",default=None)
  created_date = models.DateTimeField(null=True,db_column='created_date',auto_now_add=True)
  
  class Meta:
        db_table='company'
        ordering = ('-id',)

class company_summary(models.Model):
  file_name = models.CharField(max_length=100,null=True,blank=True,db_column='file_name')
  added_by = models.CharField(max_length=200,null=True,blank=True,db_column='added_by')
  total_count = models.IntegerField(null=True,blank=True,db_column='total_count')
  created_date = models.DateTimeField(null=True,db_column='created_date',auto_now_add=True)
  
  class Meta:
        db_table='company_summary'
        ordering = ('-id',)