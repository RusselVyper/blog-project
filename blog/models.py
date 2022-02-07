from django.db import models
from django.conf import settings


class Blog(models.Model):  
    author = models.CharField(max_length=200, blank=True, null=True) 
    title = models.CharField( max_length=200, blank=True, null=True)
    images = models.ImageField(upload_to='images', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    period = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title


class Comments(models.Model):  
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.TextField(blank=True, null=True) 

