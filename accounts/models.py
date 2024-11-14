from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, BaseUserManager
from family.models import FamilyInfo

# Create your models here.
class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    user_id = models.BigAutoField(primary_key=True)
    username = None
    email = models.EmailField(unique=True, max_length=255)
    family = models.ForeignKey(FamilyInfo, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50, default="")
    profile_img=models.ImageField(upload_to='%Y%m%d/', blank=True, default='')
    profile_aggrement = models.BooleanField(default=False) # 선택약관 동의여부

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
    
class Badge(models.Model):
    badge_id = models.BigAutoField(primary_key=True)
    badge_name = models.CharField(max_length=20, default="")

class AcquiredBadge(models.Model):
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)
    family = models.ForeignKey(FamilyInfo, on_delete=models.CASCADE)