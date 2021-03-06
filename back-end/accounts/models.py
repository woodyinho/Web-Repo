from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

import datetime
import base64

"""
This file uses to extend django user table and add more attrubutes
Last modifcation 15/1/2019 
"""

#gender enum validation
gender_CHOICES = [
        ('M','Male'),
        ('F','Female')
]

def upload_path(instance, filename):
    ext = filename.split('.')[-1] 
    new_filename = "{}{}{}".format(instance.user.username, ".", ext)
    return '/'.join(["profile-pictures", new_filename])

class Profile(models.Model):

    #Every user have a profile
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="profile")

    #Personal Info
    dateOfBirth = models.DateField(auto_now=False,auto_now_add=False,null=True,blank=True)
    gender = models.CharField(
                    max_length=1,
                    choices = gender_CHOICES,
                    default = 'M'
                )
    phone = models.CharField(max_length=20)

    #Location
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    #General Health info
    height = models.SmallIntegerField(
                    default = 40,
                    validators = [MaxValueValidator(300),MinValueValidator(10)]
                )
    weight = models.SmallIntegerField(
                    default = 40,
                    validators = [MaxValueValidator(300),MinValueValidator(10)]
                )
    smoking = models.BooleanField(default = False)

    profile_picture  = models.FileField(upload_to=upload_path, max_length=255, null=True, blank=True)



    def __str__(self):
        return self.user.username

   
    #create for first time
    @receiver(post_save,sender = User)
    def create_user_profile(sender, instance,created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
    
    #update exist profile
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance,created, **kwargs):
        instance.profile.save()

 