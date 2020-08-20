from django.db import models

# Create your models here.
class Post(models.Model):
    name=models.CharField(max_length=200)
    surname=models.TextField()
    date=models.TextField()
    time=models.TextField()

