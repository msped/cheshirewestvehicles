from django.db import models

# Create your models here.

class galleryItem(models.Model):
    """Gallery Item"""
    make = models.CharField(max_length=45)
    model = models.CharField(max_length=45)
    trim = models.CharField(max_length=45)
    year = models.IntegerField()
    power = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return f'{self.id} {self.make} {self.model} {self.trim}'


class galleryImages(models.Model):
    """Image for galleryItem"""
    item = models.ForeignKey(galleryItem, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gallery')
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id} {self.item}'