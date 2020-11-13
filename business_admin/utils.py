import os
from django.template.loader import render_to_string
from django.shortcuts import redirect
from django.core.mail import EmailMessage
from django.contrib import messages
from django.http import HttpResponse
from xhtml2pdf.pisa import pisaDocument
from io import BytesIO


def get_parts(request):
    parts = {}

    for x in range(1, len(request.POST)):
        if request.POST.get('description-' + str(x)):
            row = {}
            row['description'] = request.POST.get('description-' + str(x))
            row['qty'] = request.POST.get('qty-' + str(x))
            row['unit'] = request.POST.get('unit-' + str(x))
            row['line'] = request.POST.get('line-' + str(x))
            parts[str(x)] = row
        else:
            break
    
    return parts

def create_data_structure(request):
    data = {
        'customer': {
            'name': request.POST.get('name'),
            'phone_number': request.POST.get('phone_number'),
            'email': request.POST.get('email'),
            'address_line_1': request.POST.get('address_line_1'),
            'address_line_2': request.POST.get('address_line_2'),
            'town_city': request.POST.get('town_city'),
            'county': request.POST.get('county'),
            'postcode': request.POST.get('postcode')
        },
        'vehicle': {
            'make': request.POST.get('make'),
            'model': request.POST.get('model'),
            'year': request.POST.get('year'),
            'mileage': request.POST.get('mileage')
        },
        'labour': {
            'qty': request.POST.get('labour-qty'),
            'unit': request.POST.get('labour-unit'),
            'total': request.POST.get('labour-total'),
        },
        'total': request.POST.get('invoice-total'),
        'comments': request.POST.get('comments'),
    }

    data['parts'] = get_parts(request)

    return data

def render_to_pdf(data):
    template_src = 'invoice_template/invoice_template.html'
    template = render_to_string(template_src, {'invoice': data})
    result = BytesIO()
    pdf = pisaDocument(BytesIO(template.encode("utf-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf') 
    return None

def invoice_handler(request): 
    data = create_data_structure(request)
    if request.POST.get('print') == "Print Document":
        pdf = render_to_pdf(data)
        response = HttpResponse(pdf.getvalue(), content_type="application/pdf")
        response['Content-Disposition'] = 'attachment; filename=invoice.pdf'
        return response
    else: 
        pdf = render_to_pdf(data)
        message = 'Hello,\n\nPlease see attached invoice for services by Cheshire West Vehicles.\n\nMany Thanks,\n\nCheshireWestVehicles'
        email = EmailMessage('Invoice for Services | Cheshire West Vehicles', message, 'noreply@cheshirewestvehicles.co.uk', [data['customer']['email']])
        email.attach('invoice.pdf', pdf.getvalue(), 'application/pdf')
        email.send()
        messages.success(request, f"Invoice sent by email to {data['customer']['email']}.")
        return redirect('create_invoice')