from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,BaseUserManager)
from django.contrib.auth.models import PermissionsMixin

# Create your models here.

class AccountManager(BaseUserManager):
    def create_user(self,email,full_name=None,password=None , is_active=True,is_staff=False,is_admin=False):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        if not password:
            raise ValueError('Users must have an password ')

        user_object = self.model(
            email=self.normalize_email(email),
            full_name=full_name,

        )

        user_object.set_password(password)
        user_object.staff =is_staff
        user_object.admin = is_admin
        user_object.active = is_active

        user_object.save(using=self._db)
        return user_object

    def create_staffuser(self, email,e, password,full_name=None):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            full_name =full_name,
            password=password,
            is_staff=True
        )

        user.save(using=self._db)
        return user

    def create_superuser(self, email, password,full_name=None):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            full_name = full_name,
            password=password,
            is_staff = True,
            is_admin = True,
        )

        user.save(using=self._db)
        return user

class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255,unique=True)
    full_name = models.CharField(max_length=25,blank=True,null=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)  # a admin user; non super-user
    admin = models.BooleanField(default=False)  # a superuser

    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    objects = AccountManager()

    def get_full_name(self):
        # The user is identified by their email address
        if self.full_name:
            return self.full_name
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    def __str__(self):  # __unicode__ on Python 2
        return self.email

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active