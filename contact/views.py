from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.views import View
from django.contrib import messages
from .forms import ContactForm

# Create your views here.

class Contact(View):
    template_name = "contact.html"
    def get(self, request):
        form = ContactForm()
        return render(request,self.template_name, {'form': form})
    
    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone_number']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            message += f'\nName: {name}\nfrom: {email}\nPhone Number: {phone}'
            send_mail(
                subject=subject,
                message=message,
                from_email='test@gmail.com',
                recipient_list=['matt@mspe.com',],
                fail_silently=True
            )
            messages.success(request, "Message sent, we'll contact you as soon as we can.")
            return redirect('contact')
