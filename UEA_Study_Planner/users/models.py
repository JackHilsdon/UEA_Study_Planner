from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class ToDo(models.Model):
	module_title = models.CharField(max_length=30)
	topic = models.CharField(max_length=30)
	date_created = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	notes = models.TextField()

	def __str__(self):
		return self.module_title

	def get_absolute_url(self):
		return reverse('todo')



