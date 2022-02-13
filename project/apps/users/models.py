from django.db import models

from .managers import UserManager

from django.contrib.auth.models import (
  BaseUserManager, AbstractBaseUser
)


class User(AbstractBaseUser):
  email = models.EmailField(
    max_length=255, 
    unique=True, 
    verbose_name='Email Adress'
  )
  is_active = models.BooleanField(default=True)
  is_admin = models.BooleanField(default=False)

  objects = UserManager()

  USERNAME_FIELD = 'email'

  def has_perm(self, perm, Obj=None):
    return True

  def has_module_perms(self, app_label):
    return True

  def __str(self):
    return self.email

  @property
  def is_staff(self):
    return self.is_admin
