from django.db import models
import array
class Client(models.Model):
	username = models.CharField(max_length=100,default='',unique=True)
	password = models.CharField(max_length=100,default='')

	def __str__(self):
		return self.username

class Message(models.Model):

	userfrom = models.CharField(max_length=100,default='')
	userto = models.CharField(max_length=100,default='')
	header = models.CharField(max_length=100,default='')
	message = models.TextField()

	def __str__(self):
		return self.header



