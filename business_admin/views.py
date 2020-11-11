from django.shortcuts import render
from .utils import invoice_handler

# Create your views here.

def create_invoice(request):
    if request.method == "POST":
        invoice_handler(request)
    return render(request, "create_invoice.html")
