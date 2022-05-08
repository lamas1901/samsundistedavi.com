from django.contrib import admin
from .models import Doctor,Service,Slide,CustomPage,Media,Special

# Register your models here.

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name_surname',)
    ordering = ('name_surname',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title',)
    ordering = ('title',)
    prepopulated_fields = {'slug':('title',)}

@admin.register(Special)
class SpecialAdmin(admin.ModelAdmin):
    list_display = ('title',)
    ordering = ('title',)
    prepopulated_fields = {'slug':('title',)}

@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = ('title','subtitle')
    order = ('title','subtitle')

@admin.register(CustomPage)
class CustomPageAdmin(admin.ModelAdmin):
    list_display = ('menu_name',)
    order = ('menu_name',)
    prepopulated_fields = {'slug':('menu_name',)}

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('name',)
    order = ('name',)