from django.db import models

# Create your models here.

class News(models.Model):
    title = models.TextField()
    content =  models.TextField()