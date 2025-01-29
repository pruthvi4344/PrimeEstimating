from django.db import models

# Create your models here.
class User(models.Model):
   username = models.EmailField(max_length=100)
   password = models.CharField(max_length=50)
   
class Service(models.Model):
    name = models.CharField(max_length=50)
    detail = models.CharField(max_length=1000)
    icon_class = models.CharField(max_length=100, default="fas fa-cogs")
    def __str__(self):
     return self.name
    
class About(models.Model):
   story = models.CharField(max_length=1000)
   
    
class Contact(models.Model):
   email = models.CharField(max_length=50)
   contnum = models.CharField(max_length=50)
   address = models.CharField(max_length=50)
   timing = models.CharField(max_length=50)

class Indexmanage(models.Model):
    title = models.CharField(max_length=50)
    line = models.CharField(max_length=100)
    button_text = models.CharField(max_length=10)
    background_image = models.ImageField(upload_to='indexwelcome/', blank=True, null=True)

class Servicemanage(models.Model):
    title = models.CharField(max_length=50)
    line = models.CharField(max_length=100)
    button_text = models.CharField(max_length=10)
    background_image = models.ImageField(upload_to='servicewelcome/', blank=True, null=True)

class Aboutmanage(models.Model):
    title = models.CharField(max_length=50)
    line = models.CharField(max_length=100)
    button_text = models.CharField(max_length=10)
    background_image = models.ImageField(upload_to='aboutwelcome/', blank=True, null=True)

class Contactmanage(models.Model):
    title = models.CharField(max_length=50)
    line = models.CharField(max_length=100)
    button_text = models.CharField(max_length=10)
    background_image = models.ImageField(upload_to='contactwelcome/', blank=True, null=True)