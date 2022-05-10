from django import template
from django.utils.safestring import mark_safe
import markdown

from .. import consts
from ..models import CustomPage, Service, Media, Special

register = template.Library()

@register.filter(name='markdown')
def markdown_format(text):
	return mark_safe(markdown.markdown(text))

@register.filter(name='get_const')
def get_const(const_name):
	return consts.__dict__.get(const_name,None)

@register.simple_tag
def get_header_pages():
	pages = CustomPage.objects.all().filter(show_in_header=True)
	return pages

@register.simple_tag
def get_header_services():
	services = Service.objects.all()
	return services

@register.simple_tag
def get_footer_pages():
	pages = CustomPage.objects.all().filter(show_in_footer=True)
	return pages

@register.inclusion_tag('clinic/component/services_sidebar.html')
def show_services_sidebar(services=None):
	if not services:
		services = Service.objects.all()
	return {
		'services':services,
	}

@register.simple_tag
def get_media():
	media = Media.objects.all()
	return media

# striptags

@register.simple_tag
def strip_tags(string):
	symbols = ['`','*','_','{','}','[]','()','#','+','-','.','!']
	for symbol in symbols:
		string = string.replace(sybmol,'')