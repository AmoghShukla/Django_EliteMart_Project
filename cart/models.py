from django.db import models
from django.contrib.auth.models import User
from electronics.models import Product as ElectronicsProduct
from clothing.models import product as ClothingProduct
from grocery.models import Product as GroceryProduct

class CartItem(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product_id = models.PositiveIntegerField()
    product_name = models.CharField(max_length=255)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_image = models.ImageField(upload_to="cart_images/", null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    category = models.CharField(max_length=50)  # 'electronics', 'clothing', 'grocery'

    def total_price(self):
        return self.quantity * self.product_price

    def __str__(self):
        return f"{self.product_name} ({self.quantity})"
