from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class Player(AbstractUser):
    pass


class Character(models.Model):
    pass
