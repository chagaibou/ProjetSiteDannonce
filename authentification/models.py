from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
# Create your models here.

class User(AbstractUser):
    telephoneRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    telephone = models.CharField(validators = [telephoneRegex], max_length = 16, unique = True)

