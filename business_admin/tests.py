from django.test import TestCase
from django.core import mail
from django.contrib.auth.models import User
from .apps import BusinessAdminConfig

# Create your tests here.

class TestBusinessAdminApp(TestCase):

    def setUp(self):
        User.objects.create_superuser('admin', 'admin@gmail.com', 'testpassword')

    def test_business_admin_app(self):
        """Test Business Admin App"""
        self.assertEqual("business_admin", BusinessAdminConfig.name)

    def test_create_invoice_response_get_when_logged_in(self):
        """Test the response of the create invoice page when logged in"""
        self.client.post(
            '/admin/login/',
            {
                'username': 'admin',
                'password': 'testpassword'
            },
            follow=True
        )
        response = self.client.get('/business-admin/create/invoice')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h1>Create an Invoice</h1>', response.content)

    def test_create_invoice_response_get_when_not_logged_in(self):
        """Test the response of the create invoice page when not logged in"""
        response = self.client.get('/business-admin/create/invoice', follow=True)
        self.assertIn(b'<a href="/admin/">Django administration</a>', response.content)

    def test_create_invoice_response_post(self):
        """Test the response after post"""
        self.client.post(
            '/admin/login/',
            {
                'username': 'admin',
                'password': 'testpassword'
            },
            follow=True
        )
        post_data = {
            'name': 'Matt Edwards',
            'phone_number': '07000001234',
            'email': 'test@gmail.com',
            'address_line_1': '1 Coding Lane',
            'town_city': 'London',
            'county': 'Essex',
            'postcode': 'L9 8TT',
            'make': 'Mercedes',
            'model': 'A Class',
            'year': '2013',
            'mileage': '74000',
            'labour-qty': '10',
            'labour-unit': '20',
            'labour-total': '200',
            'total': '1200.00',
            'comments': 'Test comments',
            'description-1': 'Gearbox',
            'qty-1': '1',
            'unit-1': '650',
            'line-1': '650',
            'description-2': 'Clutch',
            'qty-2': '1',
            'unit-2': '350',
            'line-2': '350',
            'send-email': 'Send via E-mail'
        }
        response = self.client.post(
            '/business-admin/create/invoice',
            post_data,
            follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Invoice sent by email to test@gmail.com.", response.content)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Invoice for Services | Cheshire West Vehicles')
        