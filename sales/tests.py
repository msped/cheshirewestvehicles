from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .apps import SalesConfig
from .forms import ReserveContactForm
from .models import Vehicle, VehicleImages

# Create your tests here.

class TestSalesApp(TestCase):

    def test_sales_app(self):
        """Test Sales App"""
        self.assertEqual("sales", SalesConfig.name)

class TestModels(TestCase):
    """Test Sales app models"""

    def vehicle_str(self):
        obj = Vehicle.objects.create(
            slug='vehicle-slug-1',
            make='Mercedes',
            model='A Class',
            trim='A250',
            year=2014,
            fuel='1',
            body_type='2',
            mileage=73000,
            engine_size=1991,
            mot_expiry='2020-12-12',
            extras='Here are some optional extras that are on this car.',
            price=13500
        )
        self.assertEqual(str(obj), '1 Mercedes A Class A250 - £13500')
    
    def image_str(self):
        """Test image model"""
        image = SimpleUploadedFile(
            "test.png",
            b'abunchofbytes'
        )
        vehicle = Vehicle.objects.get(id=1)
        vi = VehicleImages.objects.create(
            image=image,
            vehicle=vehicle
        )
        self.assertEqual(str(vi), '1 - 1')

    def test_models_in_order(self):
            self.vehicle_str()
            self.image_str()

class TestForm(TestCase):
    """Test App Forms"""
    def test_reserve_form_valid_response(self):
        """Test full working reserve form"""
        form = ReserveContactForm({
            'email': 'test@email.com',
            'name': 'John Doe',
            'phone_number': '07000000000'
        })
        self.assertTrue(form.is_valid())

    def test_reserve_form_invalid_email(self):
        """Test full working reserve form"""
        form = ReserveContactForm({
            'email': 'testemail.com',
            'name': 'John Doe',
            'phone_number': '07000000000'
        })
        self.assertFalse(form.is_valid())

    def test_reserve_form_invalid_name(self):
        """Test full working reserve form"""
        form = ReserveContactForm({
            'email': 'test@email.com',
            'name': '',
            'phone_number': '07000000000'
        })
        self.assertFalse(form.is_valid())

    def test_reserve_form_invalid_phone(self):
        """Test full working reserve form"""
        form = ReserveContactForm({
            'email': 'test@email.com',
            'name': 'John Doe',
            'phone_number': '07000a00000'
        })
        self.assertFalse(form.is_valid())

    def test_reserve_form_empty(self):
        """Test empty reserve form"""
        form = ReserveContactForm({
            'email': '',
            'name': '',
            'phone_number': ''
        })
        self.assertFalse(form.is_valid())


class TestViews(TestCase):
    
    def setUp(self):
        obj = Vehicle.objects.create(
            slug='mercedes-a-class-a250-1-13500',
            make='Mercedes',
            model='A Class',
            trim='A250',
            year=2014,
            fuel='1',
            body_type='2',
            mileage=73000,
            engine_size=1991,
            mot_expiry='2020-12-12',
            extras='Here are some optional extras that are on this car.',
            price=13500
        )
        obj.save()

    def test_vehicle_detail_response(self):
        """Test return of vehicle detail page
        should return 200"""
        response = self.client.get('/buy/mercedes-a-class-a250-1-13500/')
        self.assertEqual(response.status_code, 200)

    def test_vehicle_detail_post_to_reserve(self):
        """Test post to reserve a vehicle"""
        response = self.client.post(
            '/buy/mercedes-a-class-a250-1-13500/',
            {
                'email': 'test@email.com',
                'name': 'John Doe',
                'phone_number': '07000000000'
            },
            follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Reserved',
            response.content
        )

    def test_used_cars_page(self):
        """Test response of for sale page"""
        response = self.client.get('/buy/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h1 class="text-center">Used Cars</h1>', response.content)