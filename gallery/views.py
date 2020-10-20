from django.shortcuts import render
from .models import galleryItem, galleryImages

# Create your views here.

def gallery(request):
    featured = galleryItem.objects.all().order_by('-id')
    images = galleryImages.objects.all()
    context = {
        'featured': featured,
        'images': images
    }
    return render(request, "gallery.html", context)

def gallery_detail(request, gallery_slug):
    vehicle = galleryItem.objects.get(slug=gallery_slug)
    images = galleryImages.objects.filter(item=vehicle)
    context = {
        'vehicle': vehicle,
        'images': images
    }
    return render(request, "gallery_detail.html", context)