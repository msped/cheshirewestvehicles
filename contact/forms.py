from django import forms
from django.core.validators import RegexValidator

class ContactForm(forms.Form):
    """Contact form"""
    phone_regex = RegexValidator(
        regex='^[0-9]*$',
        message='Please enter a phone number.',
        code='invalid_phone'
    )
    name = forms.CharField(max_length=50, required=True)
    phone_number = forms.CharField(max_length=11, required=True, validators=[phone_regex])
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': 'Please describe any repairs in as much detail as possible.'}
        ),
        required=True
    )