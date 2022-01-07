from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE) #if user deleted, post is deleted

    def __str__(self):
        return self.title

#Redirect Method will redirect you to a specific route in General. 
#Reverse Method will return the complete URL to that route as a String.
    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})

