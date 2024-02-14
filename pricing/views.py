from django.shortcuts import render
from django.http import JsonResponse
from .models import PricingConfig
from decimal import Decimal

# Create your views here.
def calculate_price(request):
    if request.method== 'GET':
        distance_traveled = Decimal(request.GET.get('distance_traveled', 0))
        time_traveled = Decimal(request.GET.get('time_traveled', 0))
        waiting_time = Decimal(request.GET.get('waiting_time', 0))

        day_of_week = request.GET.get('day_of_week', 'Mon')

        try: 
            pricing_config = PricingConfig.objects.get(day_of_week=day_of_week, enabled=True)
        except PricingConfig.DoesNotExist:
            return JsonResponse({"error": "No pricing configuration found for the provided day of the week"}, status=400)
        
        dbp = Decimal(pricing_config.distance_base_price)
        dap = Decimal(pricing_config.distance_additional_price)
        tmf = Decimal(pricing_config.time_multiplier_factor)
        wc = Decimal(pricing_config.waiting_charges)

        # Perform calculations using Decimal objects
        additional_distance_charge = max(distance_traveled - Decimal('3'), Decimal('0')) * dap
        time_multiplier_charge = max(time_traveled - Decimal('60'), Decimal('0')) * tmf
        waiting_charge = (waiting_time // Decimal('3')) * wc

        # Calculate total price
        price = (dbp + additional_distance_charge) + time_multiplier_charge + waiting_charge

        return JsonResponse({"price": price})
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)