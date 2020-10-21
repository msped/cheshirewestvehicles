from django.urls import path
from .views import gallery, gallery_detail

urlpatterns = [
    path('', gallery, name="gallery"),
    path('<slug:gallery_slug>/', gallery_detail, name="gallery_detail")
]