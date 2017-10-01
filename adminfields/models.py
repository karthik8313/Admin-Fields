from django.db import models

class post1(models.Model):
	First_Name=models.CharField(max_length=30,blank=True)
	Middle_Name=models.CharField(max_length=30,blank=True)
	Last_Name=models.CharField(max_length=30,blank=True)
	image=models.ImageField(upload_to="media/images")
	content=models.TextField(max_length=300,blank=True)
	email=models.EmailField(max_length=30,blank=True)

