from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save,sender=User) #when a user is saved, then send post_save signal that is received by the reciever i.e. create_profile function
def create_profile(sender,instance,created,**kwargs): #kwargs accepts any additional keywords at end of argument of function
    if created:
        Profile.objects.create(user=instance) #instance is instance of the user created

@receiver(post_save,sender=User) 
def save_profile(sender,instance,**kwargs):
    instance.profile.save()
