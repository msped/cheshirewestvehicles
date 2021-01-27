import os
from django.shortcuts import render, redirect
from django.views import View
from django.core.paginator import Paginator
from django.contrib import messages
from django.http import HttpResponse
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.conf import settings
from .models import Vehicle, VehicleImages
from .forms import ReserveContactForm

# Create your views here.

class Vehicles(View):
    """Show all vehicles"""
    template_name = 'buy.html'
    def get(self, request):
        sort_options = request.GET.get('sort_options')
        if sort_options:
            vehicles = Vehicle.objects.all().order_by(sort_options)
        else:
            vehicles = Vehicle.objects.all().order_by('reserved')
        paginator = Paginator(vehicles, 10)
        page_number = request.GET.get('page')
        vehicle_obj = paginator.get_page(page_number)
        images = VehicleImages.objects.all().order_by('id')
        context = {
            'vehicles': vehicle_obj,
            'images': images
        }
        return render(request, self.template_name, context)

class VehicleDetail(View):
    template_name = 'vehicle_detail.html'
    def get(self, request, vehicle_slug):
        vehicle = Vehicle.objects.get(slug=vehicle_slug)
        images = VehicleImages.objects.filter(vehicle=vehicle)
        form = ReserveContactForm()
        context = {
            'vehicle': vehicle,
            'images': images,
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request, vehicle_slug):
        vehicle = Vehicle.objects.get(slug=vehicle_slug)
        form = ReserveContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            vehicle.reserved = '2'
            vehicle.save()
            messages.success(
                request,
                'You have reserved this vehicle. We will contact you for deposit payment.'
            )
            standard_string = f'<p>Please contact {name} ({email}) on {phone_number} to reserve {vehicle.id} {vehicle.make} {vehicle.model} {vehicle.trim} £{vehicle.price}</p>'
            if request.POST.get('trade-in', False):
                make = request.POST.get('make')
                model = request.POST.get('model')
                trim = request.POST.get('trim')
                year = request.POST.get('year')
                mileage = request.POST.get('mileage')
                comments = request.POST.get('comments')
                standard_string += f' <p>Trade-in vehicle:</p>\
                    <p>\
                        Make: {make}\
                        Model: {model}\
                        Trim: {trim}\
                        Year: {year}\
                        Mileage: {mileage}\
                        Comments: \n{comments}\
                    </p>'
            # message = Mail(
            # from_email=settings.DEFAULT_FROM_EMAIL,
            # to_emails='autoskunkworks@gmail.com',
            # subject=f'Reserve vehicle request {vehicle.id} {vehicle.make} {vehicle.model} {vehicle.trim} £{vehicle.price}',
            # html_content=standard_string)
            # try:
            #     sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            #     response = sg.send(message)
            # except Exception as e:
            #     print(e)
        return redirect('vehicle_detail', vehicle_slug=vehicle_slug)

def check_sale_state(request, vehicle_id):
    """Check sale state to see if has updated"""
    vehicle = Vehicle.objects.get(id=vehicle_id)
    return HttpResponse(str(vehicle.get_reserved_display()))
