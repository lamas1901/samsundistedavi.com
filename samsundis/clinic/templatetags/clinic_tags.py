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

@register.inclusion_tag('clinic/component/header_pages.html')
def show_header_pages(page):
	pages = CustomPage.objects.all().filter(show_in_header=True)
	return {
		'header_pages':pages,
		'current_page':page
	}

@register.inclusion_tag('clinic/component/header_services.html')
def show_header_services():
	services = Service.objects.all()
	return {
		'services':services
	}

@register.inclusion_tag('clinic/component/footer_pages.html')
def show_footer_pages():
	pages = CustomPage.objects.all().filter(show_in_footer=True)
	return {
		'footer_pages': pages,
	}

@register.inclusion_tag('clinic/component/services_sidebar.html')
def show_services_sidebar(services=None):
	if not services:
		services = Service.objects.all()
	return {
		'services':services,
	}

@register.inclusion_tag('clinic/component/media.html')
def show_media():
	media = Media.objects.all()
	return {
		'media':media
	}

# specials

@register.simple_tag
def get_specials():
	return Special.objects.all()

# striptags

@register.simple_tag
def strip_tags(string):
	symbols = ['`','*','_','{','}','[]','()','#','+','-','.','!']
	for symbol in symbols:
		string = string.replace(sybmol,'')