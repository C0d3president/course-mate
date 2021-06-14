from django.db import models
from datetime import datetime    
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User

# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError(" User must have an email address")
        if not username:
            raise ValueError(" User must have an username!")    
        
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password = password,
            username=username,
        )
        user.email = email
        user.is_admin = True 
        user.is_staff = True 
        user.is_superuser = True 
        user.save(using=self._db)
        return user

class Users(AbstractBaseUser):
    username = models.CharField( max_length=20, unique=True)  
    email = models.CharField( max_length=50, unique=True)    
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(default=timezone.now)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    name = models.CharField( max_length=60, null=True)
    phone = models.CharField(max_length=20, null=True)
    password = models.CharField( max_length=100)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [ 'email']
    
    objects=MyAccountManager()
     
    def _str_(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

        
class Questions(models.Model):
    quiz = models.CharField(max_length=50)
    user = models.CharField(max_length=50, null=True)
    date = models.DateTimeField(verbose_name='date', auto_now_add=True, null=True)
    answers = models.IntegerField(max_length=50,null=True)

class Answers(models.Model):
    answer = models.CharField(max_length=350)
    quiz_id = models.IntegerField(max_length=50,null=True)
    date = models.DateTimeField(verbose_name='date answered', auto_now_add=True, null=True)
    user = models.CharField(max_length=50, null=True)


class Courses(models.Model):
    course_name = models.CharField(max_length=50)
    user_created = models.CharField(max_length=50, null=True)

class Course_Modules(models.Model):
    moduleName = models.CharField(max_length=50)
    description = models.CharField(max_length=50, null=True)
    link = models.CharField(max_length=50, null=True)
    course_id = models.IntegerField(max_length=100,null=True)
    user_created = models.CharField(max_length=50, null=True)
