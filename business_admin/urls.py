from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import CreateInvoice

urlpatterns = [
    path('create/invoice', login_required(CreateInvoice.as_view()), name="create_invoice"),
]