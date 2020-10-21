from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .apps import GalleryConfig
from .models import galleryItem, galleryImages

# Create your tests here.

class TestGalleryApp(TestCase):

    def test_gallery_app(self):
        """Test gallery App"""
        self.assertEqual("gallery", GalleryConfig.name)

class TestModels(TestCase):
    """Test gallery app models"""

    def galleryitem_str(self):
        obj = galleryItem.objects.create(
            slug='gallery-slug-1',
            make='Mercedes',
            model='A Class',
            trim='A250',
            year=2014,
            power=500,
            description="A description of the build."
        )
        self.assertEqual(str(obj), '1 Mercedes A Class A250')
    
    def image_str(self):
        """Test image model"""
        image = SimpleUploadedFile(
            "test.png",
            b'abunchofbytes'
        )
        gallery = galleryItem.objects.get(id=1)
        gi = galleryImages.objects.create(
            image=image,
            item=gallery
        )
        self.assertEqual(str(gi), '1 1 Mercedes A Class A250')

    def test_models_in_order(self):
            self.galleryitem_str()
            self.image_str()

class TestViews(TestCase):
    
    def setUp(self):
        obj = galleryItem.objects.create(
            slug='mercedes-a-class-a250-500',
            make='Mercedes',
            model='A Class',
            trim='A250',
            year=2014,
            power=500,
            description="A description of the build."
        )
        obj.save()

    def test_gallery_detail_response(self):
        """Test return of gallery detail page
        should return 200"""
        response = self.client.get('/gallery/mercedes-a-class-a250-500/')
        self.assertEqual(response.status_code, 200)

    def test_gallery(self):
        """Test response of for gallery page"""
        response = self.client.get('/gallery/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h1 class="text-center">Featured Gallery</h1>', response.content)