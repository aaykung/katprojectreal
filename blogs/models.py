from django.db import models

# Create your models here.
class Post(models.Model):
    name=models.CharField(max_length=200)
    desc=models.TextField()

class Maindata(models.Model):
    ชื่อ=models.CharField(max_length=200)
    นามสกุล=models.CharField(max_length=200)
    วันที่=models.CharField(max_length=200)
    เวลา=models.CharField(max_length=200)

