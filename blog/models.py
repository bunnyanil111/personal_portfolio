from django.db import models
class Blog(models.Model):
	title=models.CharField(max_length=50)
	description=models.TextField(max_length=150)
	#date=models.DateField()


# Create your models here.
