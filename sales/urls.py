from django.urls import path
from .views import vehicles, vehicle_detail

urlpatterns = [
    path('', vehicles, name="vehicles"),
    path('<slug:vehicle_slug>/', vehicle_detail, name="vehicle_detail")
]