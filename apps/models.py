from django.db import models

# Create your models here.
class newdb(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to="profile",null=True, blank=True)
class admindb(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    mob = models.IntegerField(max_length=100, null=True, blank=True)
    pas = models.CharField(max_length=100, null=True, blank=True)
    passwd = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to="profile", null=True, blank=True)