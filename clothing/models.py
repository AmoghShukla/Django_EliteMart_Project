from django.db import models

# Create your models here.
class product(models.Model):
    SIZE_CHOICES = [
        ('XS', 'Extra Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
        ('XXL', 'Double Extra Large'),
        ('XXXL', 'Triple Extra Large'),
    ]

    COLOR_CHOICES = [
        ('RED', 'Red'),
        ('BLU', 'Blue'),
        ('GRN', 'Green'),
        ('BLK', 'Black'),
        ('WHT', 'White'),
        ('YLW', 'Yellow'),
        ('ORG', 'Orange'),
        ('PNK', 'Pink'),
        ('PRP', 'Purple'),
        ('BRN', 'Brown'),
        ('GRY', 'Gray'),
        ('NVY', 'Navy'),
        ('TUR', 'Turquoise'),
        ('GLD', 'Gold'),
        ('SLV', 'Silver'),
    ]
    
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=4, choices=SIZE_CHOICES, default='M')
    color = models.CharField(max_length=10, choices=COLOR_CHOICES, default='Red')
    price = models.DecimalField(max_digits=10, decimal_places=1)
    image = models.ImageField(upload_to='product_img/')

    def __str__(self):
        return self.name
