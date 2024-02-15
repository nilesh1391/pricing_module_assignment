from django.contrib import admin
from .models import PricingConfig

# Register your models here.
class PricingConfigAdmin(admin.ModelAdmin):
    list_display = ('distance_base_price', 'distance_additional_price', 'time_multiplier_factor', 'waiting_charges', 'day_of_week', 'created_by')


admin.site.register(PricingConfig, PricingConfigAdmin)