from django.db import models

from django.contrib.auth.models import User

from django.template.defaultfilters import slugify

# Create your models here.

class UserProfile(models.Model):

    # This  Links UserProfile to a User model instance.

    user = models.OneToOneField(User)

    # The additional attributes we wish to include outside the User model instance 
    
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username


# Law Prof Category 

class ProfessionalCategory(models.Model): 
	name = models.CharField(max_length=128, unique=True) 
	slug = models.SlugField(unique=True, blank=True)

	def save(self, *args, **kwargs): 
		self.slug = slugify(self.name) 
		super(ProfessionalCategory, self).save(*args, **kwargs)


	def __unicode__(self): #For Python 2, use __str__ on Python 3

		return self.name



# Location  

class Location(models.Model): 
	name = models.CharField(max_length=50) 
	slug = models.SlugField(unique=True, blank=True)

	def save(self, *args, **kwargs): 
		self.slug = slugify(self.name) 
		super(Location, self).save(*args, **kwargs)


	def __unicode__(self): #For Python 2, use __str__ on Python 3 

		return self.name




# Professionals 

class Professional(models.Model): 
	category = models.ForeignKey(ProfessionalCategory) 
	name = models.CharField(max_length=128) 
	email = models.CharField(max_length=128) 
	phone = models.CharField(max_length=64) 
	address = models.CharField(max_length=128) 
	location = models.ForeignKey(Location) 
	url = models.URLField() 
	views = models.IntegerField(default=0) 
	slug = models.SlugField(unique=True, blank=True)

	def save(self, *args, **kwargs): 
		self.slug = slugify(self.name) 
		super(Professional, self).save(*args, **kwargs)

	def __unicode__(self): #For Python 2, use __str__ on Python 3 

		return self.name
