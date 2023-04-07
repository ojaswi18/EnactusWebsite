from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    name= models.CharField(max_length=30)
    email=models.EmailField()
    message=models.TextField()
    time=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Achievement(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    desc=RichTextField(blank=True)
    slug=models.CharField(max_length=30)
    time=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


class Member(models.Model):
    sno=models.CharField(max_length=2)
    name=models.CharField(max_length=30)
    post=models.CharField(max_length=30)
    time=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to="static",default='')
    
    def __str__(self):
        return self.name    
    