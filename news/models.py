from django.db import models

class News(models.Model):
    title = models.TextField()
    content =  models.TextField()