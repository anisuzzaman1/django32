from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=250)
    content =  models.TextField()
    #status = models.CharField(max_length=250)