from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
  def _create_user(self, email, password, isAdmin=False):
    user = self.model(
      email = self.normalize_email(email),
      is_admin= isAdmin
    )

    user.set_password(password)
    user.save(using=self.db)
    return user

  def create_user(self, email, password = None):
    return self._create_user(email, password)
  
  def create_superuser(self, email, password = None):
    return self._create_user(email, password, True)