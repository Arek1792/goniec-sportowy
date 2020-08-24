from django.db import models
from django.contrib import admin

# Create your models here.

#model for articles displayed in tablica app
class Article(models.Model):
	#content of article
	title = models.CharField(max_length=150)
	description = models.CharField(max_length=300)
	paragraph = models.TextField() #mandatory text
	paragraph2 = models.TextField(blank=True)
	paragraph3 = models.TextField(blank=True)
	paragraph4 = models.TextField(blank=True)
	paragraph5 = models.TextField(blank=True)

	date = models.DateTimeField(auto_now_add=True)

	image = models.ImageField(upload_to='tablica/images/', blank=True) #optional field
	image2 = models.ImageField(upload_to='tablica/images/', blank=True) #optional field
	image3 = models.ImageField(upload_to='tablica/images/', blank=True) #optional field
	image4 = models.ImageField(upload_to='tablica/images/', blank=True) #optional field
	image5 = models.ImageField(upload_to='tablica/images/', blank=True) #optional field
	
	url = models.URLField(blank=True) #optional field
	slug = models.SlugField(unique=True)

	def __str__(self):
		return self.title

	# def save(self, *args, **kwargs):
	# 	self.slug = self.slug or slugify(self.title)
	# 	super().save(*args, **kwargs)




