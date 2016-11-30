from __future__ import unicode_literals

from django.db import models
from model_utils.managers import InheritanceManager
# Create your models here.
class Content(models.Model):
    title=models.CharField(max_length=120)
    sub_title=models.CharField(max_length=120)
    
    objects = InheritanceManager()
    
    def __unicode__(self):
        return self.title + " -- " + self.sub_title
    
class Content_Types(Content):
    element=models.CharField(max_length=120)
    content=models.TextField()
    image=models.ImageField(blank=True)
    video=models.FileField(blank=True)
    
    def __unicode__(self):
        return self.element
    