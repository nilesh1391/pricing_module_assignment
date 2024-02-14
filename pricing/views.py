from django.shortcuts import render
from django.http import JsonResponse
from .models import PricingConfig

# Create your views here.
def calculate_price(request):
    if request.method== 'GET':
        distance_traveled = float(request.GET.get('distance_traveled', 0))
        time_traveled = float(request.GET.get('time_traveled', 0))
        waiting_time = float(request.GET.get('waiting_time', 0))

        day_of_week = request.GET.get('day_of_week', 'Mon')

        try: 
            pricing_config = PricingConfig.objects.get(day_of_week=day_of_week, enabled=True)
        except PricingConfig.DoesNotExist:
            return JsonResponse({"error": "No pricing configuration found for the provided day of the week"}, status=400)
        
        dbp = pricing_config.distance_base_price
        dap = pricing_config.distance_additional_price
        tmf = pricing_config.time_multiplier_factor
        wc = pricing_config.waiting_charges

        price = (dbp + (max(distance_traveled - 3, 0)*dap)) + (max(time_traveled - 60, 0)* tmf)+(waiting_time//3*wc)
        return JsonResponse({"price": price})
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)