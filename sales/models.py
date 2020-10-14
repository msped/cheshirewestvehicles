from django.db import models
import datetime

# Create your models here.

class Vehicle(models.Model):
    """Vehicle Model"""
    RESERVE_CHOICES = (
        (u"1", u'For Sale'),
        (u"2", u'Reserved'),
        (u"3", u'Sold')
    )

    class Fuel(models.TextChoices):
        """Options for Fuel"""
        PETROL = '1', 'Petrol'
        DIESEL = '2', 'Diesel'
        HYBRID = '3', 'Hybrid'
        ELECTRIC = '4', 'Electric'
    
    class CarState(models.TextChoices):
        """State of sale"""
        TRADE_IN = '1', 'Trade-in'
        FRONTLINE = '2', 'Frontline'

    class BodyType(models.TextChoices):
        """Body Type of vehicle"""
        COUPE = '1', 'Coupe'
        HATCHBACK = '2', 'Hatchback'
        SALOON = '3', 'Saloon'
        ESTATE = '4', ' Estate'
        VAN = '5', 'Van'
        CONVERTIBLE = '6', 'Convertible'

    def current_year():
        return datetime.date.today().year

    slug = models.SlugField(unique=True, null=True, blank=True)
    make = models.CharField(max_length=15)
    model = models.CharField(max_length=15)
    trim = models.CharField(max_length=30)
    year = models.IntegerField(choices=[(x, str(x)) for x in range(1980,datetime.date.today().year+1)], default=current_year)
    fuel = models.CharField(max_length=8, choices=Fuel.choices, default='1')
    body_type = models.CharField(max_length=8, choices=BodyType.choices, default='1')
    car_state = models.CharField(max_length=8, choices=CarState.choices, default='1')
    reserved = models.CharField(max_length=8, choices=RESERVE_CHOICES, default='2')
    mileage = models.IntegerField()
    engine_size = models.IntegerField()
    mot_till = models.DateField()
    extras = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f'{self.id} {self.make} {self.model} {self.trim} - £{self.price}'

class VehicleImages(models.Model):
    """Images relating to a vehicle"""
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='vehicle_images')
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.vehicle.id} - {self.id}'
