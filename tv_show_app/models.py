from __future__ import unicode_literals
from django.db import models
import datetime


# Create your models here.

class ShowManager(models.Manager):
    def validator(self, postData):
        errors={}
        if postData['create_or_update']=="Create":
            if Shows.objects.filter(title=postData['title']).count() > 0:
                errors['title_duplication'] = "There is already a show with this name in the database"
        
        if len (postData['title'])<2:
            errors['name']="Title must be at least 2 characters long."
        if len(postData['network'])<3:
            errors['network']="Network must be at least 3 characters long."
        if len(postData['description']) < 10 and len(postData['description'])>0:
            errors['description']="Description must be at least 10 characters long."
        if postData['release']>str(datetime.date.today()):
            errors['release']="Release date must not be in the future."
        print ('postdata: ', postData['release'], 'today: ', datetime.date.today())
            
        return errors
        
        
class Shows(models.Model):
    title = models.CharField(max_length=100)
    network = models.CharField(max_length=55)
    release_date = models.DateField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
    
    
