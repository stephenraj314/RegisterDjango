from django.db import models
from signUp.models import users


# Create your models here.
class posts(models.Model):

    user_name = models.ForeignKey(users, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=100)
    post_desc=models.CharField(max_length=1000)
