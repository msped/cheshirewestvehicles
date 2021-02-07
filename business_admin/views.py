from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .utils import invoice_handler

# Create your views here.

class CreateInvoice(View):
    template_name = "create_invoice.html"
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        email_address = invoice_handler(request)
        messages.success(request, f"Invoice sent by email to {email_address}.")
        return redirect('create_invoice')
