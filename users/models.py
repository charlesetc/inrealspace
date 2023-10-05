import nanoid
from django.contrib.auth.models import AbstractUser
from django.db import models
from functools import partial


class RealSpaceUser(AbstractUser):
    username = None
    email = models.EmailField('email address', unique=True)
    id = models.CharField(primary_key=True, max_length=15, default=partial(nanoid.generate, size=14))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
