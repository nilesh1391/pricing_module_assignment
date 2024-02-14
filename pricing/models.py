from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PricingConfig(models.Model):
    class Meta:
        db_table = 'pricing_configuration'

    price_id = models.BigAutoField(primary_key=True)
    distance_base_price = models.DecimalField(max_digits=8, decimal_places=2)
    distance_additional_price = models.DecimalField(max_digits=8, decimal_places=2)
    time_multiplier_factor = models.DecimalField(max_digits=8, decimal_places=2)
    waiting_charges = models.DecimalField(max_digits=8, decimal_places=2)
    day_of_week = models.CharField(max_length=11)
    enabled = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Pricing configuration for {self.day_of_week}"
    

