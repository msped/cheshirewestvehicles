from django.contrib import admin
from .models import galleryItem, galleryImages

# Register your models here.

class galleryImagesInlineAdmin(admin.TabularInline):
    model = galleryImages

@admin.register(galleryItem)
class galleryItemAdmin(admin.ModelAdmin):
    inlines = [galleryImagesInlineAdmin]
    prepopulated_fields = {'slug': ('make', 'model', 'trim', 'power')}

    class Meta:
        model = galleryItem

@admin.register(galleryImages)
class galleryImagesAdmin(admin.ModelAdmin):
    pass