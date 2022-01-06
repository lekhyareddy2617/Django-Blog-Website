from django.db import models
from django.contrib.auth.models import User
from PIL import Image #from pillow

class Profile(models.Model): #now we create 1-to-1 relationship btwn model and profile pic
    user=models.OneToOneField(User,on_delete=models.CASCADE) #when user is deleted, delete the profile
    image=models.ImageField(default='default.jpg',upload_to='profile_pics') #profile_pics is the directory the pics get uploaded to
    
    def __str__(self):
        return f'{self.user.username} Profile' #if username is abc it will return abc Profile
    
    def save(self):
        super().save()
        img=Image.open(self.image.path)
        if img.height>300 or img.width>300: #resize image
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
