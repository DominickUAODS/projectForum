from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    birthDate = models.DateField(null=True, verbose_name="Дата рождения", help_text="Укажите дату рождения")
