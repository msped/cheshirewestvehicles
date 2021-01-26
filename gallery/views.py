from django.shortcuts import render
from django.views import View
from .models import galleryItem, galleryImages

# Create your views here.

class Gallery(View):
    template_name = "gallery.html"
    def get(self, request):
        featured = galleryItem.objects.all().order_by('-id')
        images = galleryImages.objects.all()
        context = {
            'featured': featured,
            'images': images
        }
        return render(request, self.template_name, context)

class GalleryDetail(View):
    template_name = "gallery_detail.html"
    def get(self, request, gallery_slug):
        vehicle = galleryItem.objects.get(slug=gallery_slug)
        images = galleryImages.objects.filter(item=vehicle)
        context = {
            'vehicle': vehicle,
            'images': images
        }
        return render(request, self.template_name, context)
