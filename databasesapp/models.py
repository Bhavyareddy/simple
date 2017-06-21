from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Database(models.Model):
	fname = models.CharField(max_length = 30,null=True)
	lname = models.CharField(max_length = 30,null=True)
	phoneno = models.IntegerField(null=True)
	# password = models.CharField(max_length=30)
	
class Detials(models.Model):
	username = models.CharField(max_length = 30)
	password = models.CharField(max_length = 30)
	phoneno = models.IntegerField()