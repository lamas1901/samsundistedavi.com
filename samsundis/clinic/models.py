from django.db import models
from django.urls import reverse

# Create your models here.

class Doctor(models.Model):
    name_surname = models.CharField(max_length=50)
    bio = models.TextField()
    photo = models.ImageField(upload_to='doctor')

    def __str__(self):
        return f'Doctor : {self.name_surname}'

class Service(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=250,unique=True,null=True,blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='service')

    def get_absolute_url(self):
        return reverse('clinic:service_detail',args=[
            self.slug
        ])

    def __str__(self):
        return f'Service : {self.title}'

class Slide(models.Model):
    title = models.CharField(max_length=75)
    subtitle = models.TextField()
    show_button = models.BooleanField()
    caption_left = models.BooleanField(default=False)
    button_text = models.CharField(max_length=50,null=True,blank=True)
    button_link = models.CharField(max_length=50,null=True,blank=True)
    image = models.ImageField(upload_to='slider')

    def __str__(self):
        return f'Slide {self.title}'

class CustomPage(models.Model):
    menu_name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=250,unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to='custom_pages/images')
    show_image = models.BooleanField(default=True)
    banner = models.ImageField(upload_to='custom_pages/banners',null=True,blank=True)
    show_banner = models.BooleanField(default=False)
    show_services_sidebar = models.BooleanField(default=True)
    show_in_header = models.BooleanField()
    show_in_footer = models.BooleanField()

    def get_absolute_url(self):
        return reverse('clinic:custom_page',args=[
            self.slug
        ])

    def __repr__(self):
        return f'<CustomPage : "{self.title}">'

class Media(models.Model):
    name = models.CharField(max_length=25)
    icon_markdown = models.CharField(max_length=250)
    hex_icon_color = models.CharField(max_length=10,default="#5c85ce")
    link = models.TextField()