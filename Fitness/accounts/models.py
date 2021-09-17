from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    profile_pic = models.FileField(upload_to='static/profiles_pic', default='static/images/sample_user.jpg')
    created_date = models.DateTimeField(auto_now_add=True)
