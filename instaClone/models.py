from django.db import models

# Create your models here.

class BlogDb(models.Model):
	title = models.CharField(max_length = 255)
	post = models.ImageField(default="default.jpg")

	def __str__(self):
		return self.name