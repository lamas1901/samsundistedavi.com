from django.db import models

# Create your models here.

class Doctor(models.Model):
    name_surname = models.CharField(max_length=50)
    bio = models.TextField()
    photo = models.ImageField(upload_to='doctor')

    def __str__(self):
        return f'Doctor : {self.name_surname}'

class Service(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to='service')

    def __str__(self):
        return f'Service : {self.title}'

class Slide(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50,null=True)
    show_button = models.BooleanField()
    button_text = models.CharField(max_length=50,null=True,blank=True)
    button_link = models.CharField(max_length=50,null=True,blank=True)
    image = models.ImageField(upload_to='slider')

    def __str__(self):
        return f'Slide {self.title}'
