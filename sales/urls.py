from django.urls import path
from .views import Vehicles, VehicleDetail, check_sale_state

urlpatterns = [
    path('', Vehicles.as_view(), name="vehicles"),
    path('<slug:vehicle_slug>/', VehicleDetail.as_view(), name="vehicle_detail"),
    path('sale-state/<int:vehicle_id>', check_sale_state, name="get_sale_state"),
]