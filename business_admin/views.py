from django.shortcuts import render
from django.views import View
from .utils import invoice_handler

# Create your views here.

class CreateInvoice(View):
    template_name = "create_invoice.html"
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        invoice_handler(request)
