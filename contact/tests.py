from django.test import TestCase
from .forms import ContactForm
from .apps import ContactConfig

# Create your tests here.

class TestContactApp(TestCase):

    def test_contactt_page_response(self):
        """Test page response"""
        response = self.client.get(
            '/contact/'
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h1>Contact Us</h1>', response.content)

    def test_contact_app(self):
        """Test Contact App"""
        self.assertEqual("contact", ContactConfig.name)

    def test_form_sending(self):
        """Test sending of a contact form"""
        response = self.client.post(
            '/contact/',
            {
                'name': 'John Doe',
                'phone_number': '07000000000',
                'email': 'test@email.com',
                'subject': 'test subject',
                'message': 'test message'
            },
            follow=True
        )
        self.assertIn(b"Message sent, we&#x27;ll contact you as soon as we can.", response.content)

class TestContactForm(TestCase):
    """Contact form tests"""
    def test_contact_form_valid_response(self):
        """Test full working contact form"""
        form = ContactForm({
            'name': 'John Doe',
            'phone_number': '07000000000',
            'email': 'test@email.com',
            'subject': 'test subject',
            'message': 'test message'
        })
        self.assertTrue(form.is_valid())

    def test_contact_form_invalid_email(self):
        """Test invalid email"""
        form = ContactForm({
            'name': 'John Doe',
            'phone_number': '07000000000',
            'email': 'testemail.com',
            'subject': 'test subject',
            'message': 'test message'
        })
        self.assertFalse(form.is_valid())

    def test_contact_form_invalid_subject(self):
        """Test empty subject"""
        form = ContactForm({
            'name': 'John Doe',
            'phone_number': '07000000000',
            'email': 'test@email.com',
            'subject': '',
            'message': 'test message'
        })
        self.assertFalse(form.is_valid())

    def test_contact_form_invalid_message(self):
        """Test empty message"""
        form = ContactForm({
            'name': 'John Doe',
            'phone_number': '07000000000',
            'email': 'test@email.com',
            'subject': 'test subject',
            'message': ''
        })
        self.assertFalse(form.is_valid())

    def test_contact_form_invalid_phone_number(self):
        """Test invalid phone number"""
        form = ContactForm({
            'name': 'John Doe',
            'phone_number': '07000000a00',
            'email': 'test@email.com',
            'subject': 'test subject',
            'message': ''
        })
        self.assertFalse(form.is_valid())

    def test_contact_form_invalid_name(self):
        """Test invalid name"""
        form = ContactForm({
            'name': '',
            'phone_number': '07000000a00',
            'email': 'test@email.com',
            'subject': 'test subject',
            'message': ''
        })
        self.assertFalse(form.is_valid())    

    def test_contact_form_empty(self):
        """Test empty contact form"""
        form = ContactForm({
            'name': '',
            'phone_number': '',
            'email': '',
            'subject': '',
            'message': ''
        })
        self.assertFalse(form.is_valid())