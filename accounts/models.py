from datetime import date, datetime, timedelta
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, email, name, subscribe="free", expired_at=datetime.now()+timedelta(days=7), password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not name:
            raise ValueError('Users must have a name')

        user = self.model(
            email=self.normalize_email(email),
            name=name
        )
        user.is_active = True
        user.is_admin = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            name=name,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user



class User(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=255, unique=True)
    name = models.CharField(max_length=60)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    subscribe = models.CharField(max_length=60, null=True)
    expired_at = models.DateField(null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = MyUserManager()

    def __str__(self):
        return f"{self.email}"

    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True


class Profile (models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="profile", on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=100)
    address = models.CharField(max_length=100, null=True, blank=True)
    digital_address = models.CharField(max_length=100, null=True, blank=True)
    logo = models.ImageField(upload_to="logos", null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #Metadata
    class Meta :
        verbose_name_plural = "profiles"

    #Methods
    def __str__(self):
        return f"{self.name}"


class Activity (models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="activities", on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #Metadata
    class Meta :
        verbose_name_plural = "activities"
        ordering = ["-created_at"]

    #Methods
    def __str__(self):
        return f"{self.action}"
 