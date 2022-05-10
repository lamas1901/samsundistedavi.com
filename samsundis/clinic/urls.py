from django.urls import path
from . import views

app_name = 'clinic'

urlpatterns = [
	path('',views.home,name='home'),
	path('specials/',views.specials,name='specials'),
	path('special/<str:slug>/',views.special_single,name='special_single'),
	path('mutlu-insanlar/',views.mutlu_insanlar,name='mutlu_insanlar'),
	path('about_us/',views.about_us,name='about_us'),
	path('contact_us/',views.contact_us,name='contact_us'),
	path('service/<str:slug>/',views.service_detail,name='service_detail'),
	path('<str:slug>/',views.custom_page,name='custom_page'),
]