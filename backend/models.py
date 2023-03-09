from django.db import models

# Create your models here.
class regdb(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    mob = models.IntegerField(max_length=100, null=True, blank=True)
    pas = models.CharField(max_length=100, null=True, blank=True)
    passwd = models.CharField(max_length=100, null=True, blank=True)

class contactdb(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    subject = models.CharField(max_length=100, null=True, blank=True)
    message = models.CharField(max_length=100, null=True, blank=True)