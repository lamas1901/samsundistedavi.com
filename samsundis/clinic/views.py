from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import AppointmentForm
from .models import Doctor,Slide,Service,CustomPage,Special
from . import consts

def home(request):
	doctors = Doctor.objects.all()
	slides = Slide.objects.all()
	services = Service.objects.all()
	
	if request.method == "POST":
		form = AppointmentForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			phone = consts.__dict__.get('PHONE_WA')
			return redirect(
				f'https://api.whatsapp.com/send/?phone={ phone }&text='+
				f'{cd["name"]},{cd["phone"]},{cd["mail"]},{cd["message"]},'
			)
	else:
		form = AppointmentForm()
	
	return render(request,'clinic/home.html',{
		'doctors':doctors,
		'slides':slides,
		'services':services,
		'appointment_form':form
	})

def custom_page(request,slug):
	page = CustomPage.objects.get(slug=slug)
	return render(request,'clinic/custom_page.html',{
		'page':page	
	})

def about_us(request):
	return render(request,'clinic/about_us.html')

def contact_us(request):
	return render(request,'clinic/contact_us.html')

def service_detail(request,slug):
	service = Service.objects.get(slug=slug)
	other_services = Service.objects.all().exclude(slug=slug)
	return render(request,'clinic/service_details.html',{
		'service':service,
		'other_services':other_services
	})

def specials(request):
	return render(request,'clinic/specials.html')

def special_single(request,slug):
	special = Special.objects.get(slug=slug)
	return render(request,'clinic/special-single.html',{'special':special})