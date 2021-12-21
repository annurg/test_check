from django.db import models
from django.contrib.auth.models import User


class Client(User):
    address = models.CharField(max_length=500,)