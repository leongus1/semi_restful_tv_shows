from django.db import models

# Create your models here.
class Shows(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=55)
    release_date = models.DateField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)