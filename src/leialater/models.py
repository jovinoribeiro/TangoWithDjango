from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
#from django.template.defaultfilters import slugify


class Category(models.Model):
    name = models.CharField(max_length=128, unique = True)
    
    def __unicode__(self):
        return self.name 

class Bookmark(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128, unique = True)
    url = models.URLField()
    summary = models.CharField(max_length=500, null=True, blank=True)
    date = models.DateTimeField(default=datetime.now(), blank=True)
    #===========================================================================
    # slug = models.SlugField(unique=True)
    #  
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    #     super(Category, self).save(*args, **kwargs)
    #===========================================================================
        
    def __unicode__(self):
        return self.title
    
#===============================================================================
# class UserProfile(models.Model):
#     #user = models.ForeignKey(settings.AUTH_USER_MODEL)
#     user = models.OneToOneField(User)
#     website = models.URLField(blank=True)
#      
#     def __unicode__(self):
#         return self.to_user.username
#===============================================================================
        