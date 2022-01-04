from django.db import models

class Blog(models.Model):
    images = models.ImageField(upload_to='static/images/')
    title = models.CharField(max_length=200)
    description = models.TextField()

