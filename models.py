from django.db import models
from django.utils.timezone import now
from django.core.exceptions import ValidationError

class Product(models.Model):
    name = models.CharField(max_length=100)
    buy_price = models.DecimalField(max_digits=10, decimal_places=2)
    asking_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sold_date = models.DateField(null=True, blank=True)

    @property
    def profit(self):
        return self.selling_price - self.buy_price if self.selling_price else 0
    
    def save(self, *args, **kwargs):
        # Automatically set the sold date if selling price is set
        if self.selling_price and not self.sold_date:
            self.sold_date = now().date()
        super().save(*args, **kwargs)

    def clean(self):
        if self.buy_price <= 0:
            raise ValidationError('Buy price must be greater than 0.')
        if self.asking_price <= 0:
            raise ValidationError('Asking price must be greater than 0.')
        if self.selling_price is not None and self.selling_price <= 0:
            raise ValidationError('Selling price must be greater than 0 if provided.')
        
    

    def __str__(self):
        return self.name
