from django.contrib import admin
from .models import Doctor,Service,Slide

# Register your models here.

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name_surname',)
    ordering = ('name_surname',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title',)
    ordering = ('title',)

@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = ('title','subtitle')
    order = ('title','subtitle')

