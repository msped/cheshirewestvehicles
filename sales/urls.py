from django.urls import path
from .views import Vehicles, VehicleDetail

urlpatterns = [
    path('', Vehicles.as_view(), name="vehicles"),
    path('<slug:vehicle_slug>/', VehicleDetail.as_view(), name="vehicle_detail")
]