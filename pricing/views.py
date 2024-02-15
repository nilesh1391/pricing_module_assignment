from django.shortcuts import render
from django.http import JsonResponse
from .models import PricingConfig
from decimal import Decimal

# Create your views here.
def calculate_price(request):
    if request.method== 'GET':
        distance_traveled = request.GET.get('distance_traveled')
        time_traveled = request.GET.get('time_traveled')
        waiting_time = request.GET.get('waiting_time')

        # Check if required parameters are provided
        if distance_traveled is None or time_traveled is None or waiting_time is None:
            return JsonResponse({"error": "Required parameters missing"}, status=400)
        
        # Convert parameters to Decimal objects
        distance_traveled = Decimal(distance_traveled)
        time_traveled = Decimal(time_traveled)
        waiting_time = Decimal(waiting_time)

        try: 
            pricing_config = PricingConfig.objects.get(enabled=True)
        except PricingConfig.DoesNotExist:
            return JsonResponse({"error": "No pricing configuration found for the provided day of the week"}, status=400)
        
        dbp = Decimal(pricing_config.distance_base_price)
        print("\nDistance base price: ", dbp)
        dap = Decimal(pricing_config.distance_additional_price)
        print("\nDistance additional price : ", dap)
        tmf = Decimal(pricing_config.time_multiplier_factor)
        print("\ntime multiplier factor : ", tmf)
        wc = Decimal(pricing_config.waiting_charges)
        print("\nwaiting charge : ", wc)

        # # Perform calculations using Decimal objects
        additional_distance_charge = max(distance_traveled - Decimal('3'), Decimal('0')) * dap
        print("Additional Distance Charge :", additional_distance_charge)
        time_multiplier_charge = max(time_traveled - Decimal('60'), Decimal('0')) * tmf
        print("\ntime mulitiplier charge : ", time_multiplier_charge)
        waiting_charge = (waiting_time // Decimal('3')) * wc
        print("\nwaiting charge : ", waiting_charge)

        # Calculate total price
        price = (dbp + additional_distance_charge) + time_multiplier_charge + waiting_charge
        print("Price : ", price)

        return JsonResponse({"price": price})
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)