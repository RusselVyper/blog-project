from django.db import models


class Blog(models.Model):  
    author = models.CharField(max_length=200, blank=True, null=True) 
    title = models.CharField( max_length=200, blank=True, null=True)
    images = models.ImageField(upload_to='images', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    period = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title


