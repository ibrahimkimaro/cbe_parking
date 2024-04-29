from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin,Group,Permission
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self,email,password=None,**extra_fields):
        # extra_fields.setdefault('is_superuser', False)
        # extra_fields.setdefault('is_staff', False)
        # extra_fields.setdefault('username',False)
        if not email:
            raise ValueError(_("Please enter an email"))
        
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)
           
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('superuser is required as a staff'))
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('superuser is required as a superuser '))
        
        if extra_fields.get('is_active') is not True:
            raise ValueError(_('superuser is required as to an active s'))             
        return self.create_user(email,password,**extra_fields)
                             
class Role(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)   
    
    def __str__(self):
        
        return self.name
            
                                                  
class User(AbstractUser,PermissionsMixin):
    STATUS=(
        ('Student','Student'),
        ('Staff','Staff'),
        ('Gurdian','Gurdian'),
    )
    id = models.BigAutoField(primary_key=True, blank=True,null=False)
    username = None
    first_name = models.CharField(max_length=200,verbose_name="First Name")
    last_name = models.CharField(max_length=200,verbose_name="last name")
    email = models.EmailField(unique=True,verbose_name="Email address")
    phone_number = models.IntegerField(null=True)
    status = models.CharField(choices=STATUS,max_length=10)
    status_type = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    groups = models.ForeignKey(Role, on_delete=models.CASCADE, null=True, blank=True)
    
    objects=CustomUserManager()
    
    USERNAME_FIELD = 'email'
    EMAIL_FIELD ='email'
    REQUIRED_FIELDS = ['first_name','last_name','phone_number','status','status_type']
    
    def __str__(self):
         
        return f"{self.first_name} {self.last_name}"
    