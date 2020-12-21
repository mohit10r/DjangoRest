from django.db import models

# Create your models here.
class Course(models.Model):
	  name = models.CharField(max_length=200)
	  language = models.CharField(max_length=10)
	  price = models.CharField(max_length=7)

	  def __str__(self):
	  	return self.name 