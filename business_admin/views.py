from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .utils import invoice_handler

# Create your views here.

@login_required
def create_invoice(request):
    if request.method == "POST":
        invoice_handler(request)
    return render(request, "create_invoice.html")
