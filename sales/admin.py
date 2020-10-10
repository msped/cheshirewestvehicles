from django.contrib import admin
from django.shortcuts import render
from .models import Vehicle, VehicleImages

# Register your models here.

class VehicleImagesInlineAdmin(admin.TabularInline):
    model = VehicleImages

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    inlines = [VehicleImagesInlineAdmin]
    prepopulated_fields = {'slug': ('make', 'model', 'trim', 'fuel', 'price')}

    class Meta:
        model = Vehicle

@admin.register(VehicleImages)
class VehicleImagesAdmin(admin.ModelAdmin):
    pass