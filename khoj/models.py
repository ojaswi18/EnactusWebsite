from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class KhojInfo(models.Model):
    name=models.CharField(max_length=50)
    desc=RichTextField()
    
    def __str__(self):
        return self.name
    