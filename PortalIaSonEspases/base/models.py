from django.db import models

# Create your models here.

class userProfile(models.Model):
    username = models.CharField(max_length=150, unique=True)
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def getName(self):
        return self.username
    
    def getEmail(self):
        return self.email
    
    def getBio(self):
        return self.bio
    
    def getId(self):
        return self.id
    
    