from django.db import models
from django.contrib.auth.base_user import BaseUserManager,AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class UserManager(BaseUserManager):
    def create_user( self, email, password=None, is_staff=False, is_active=True, is_superuser=False, **extra_fields ):

        """Create a user instance with the given email and password."""
        
        email = UserManager.normalize_email(email)
        extra_fields.pop("username", None)
        user = self.model(email=email, is_active=is_active, is_staff=is_staff, is_superuser=is_superuser ,**extra_fields)
        if password:
            user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        return self.create_user( email, password, is_staff=True, is_superuser=True, **extra_fields )
    
    
    
class User(PermissionsMixin, AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100, blank=True,default="Admin")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    

    USERNAME_FIELD = "email"

    objects = UserManager()

    class Meta:
        ordering = ("email",)

    def __str__(self):
        return self.email


class APP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default="null")
    app_name=models.CharField(max_length=100, blank=True,default="")
    app_link=models.CharField(max_length=100, blank=True,default="")
    app_catrgory=models.CharField(max_length=100, blank=True,default="")
    app_sub_category=models.CharField(max_length=100, blank=True,default="")
    image=models.ImageField(default="null",blank=True,null=True)
    points=models.IntegerField( blank=True,default="")