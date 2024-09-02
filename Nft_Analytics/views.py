from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import json

def home(request):
    return render(request, 'home.html')

@csrf_exempt
def login_with_metamask(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            address = data.get('address')
            # Handle the address as needed
            return JsonResponse({'success': True})
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'Invalid JSON'}, status=400)
    return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=405)

def fetch_crypto_data(request):
    page = int(request.GET.get('page', 1))
    limit = int(request.GET.get('limit', 10))

    # API URL for CoinGecko
    api_url = f'https://api.coingecko.com/api/v3/coins/markets'
    params = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': limit,
        'page': page,
        'sparkline': 'false'
    }
    response = requests.get(api_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({'error': 'Failed to fetch data'}, status=500)



def trade_page(request):
    return render(request, 'trade.html')