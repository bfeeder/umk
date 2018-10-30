from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Comment(models.Model):
    author = models.ForeignKey(to=User,null=True,on_delete=models.SET_NULL)
    text = models.CharField(max_length=255)
    attachment = models.FileField()
    

class ToDo(models.Model):
    description = models.CharField(max_length=255)
    owner = models.ForeignKey(to=User,null=True,on_delete=models.SET_NULL)
    checked = models.BooleanField()
    deadline = models.DateTimeField()
    share = models.ManyToManyField(to=User,related_name='user')
    comments = models.ManyToManyField(to=Comment,related_name='comment',blank=True)
    attachment = models.FileField()

