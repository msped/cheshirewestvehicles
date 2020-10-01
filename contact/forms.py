from django import forms
from phonenumber_field.formfields import PhoneNumberField

class Contact(forms.Form):
    """Contact form"""
    name = forms.CharField(max_length=50, required=True)
    phone_number = PhoneNumberField()
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Please describe any repairs in as much detail as possible.'}), required=True)