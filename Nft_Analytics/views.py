from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import json
from . import views

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



def tradepage(request):
    return render(request, 'trade.html')

def sidebar_page(request):
    return render(request, 'sidebar.html')



OPENSEA_API_URL = 'https://api.opensea.io/api/v1/assets'
API_KEY = 'af46b22fcb404f39bf2703d831010401'

import requests
from django.http import JsonResponse
import requests
from django.http import JsonResponse

def generate_nft_page(request):
    return render(request, 'generate_nft.html')

import requests
import random
from django.http import JsonResponse
import requests
import random
from django.http import JsonResponse

def generate_random_nft(request):
    url = "https://api.opensea.io/api/v2/collections?chain=solana"

    headers = {
        "accept": "application/json",
        "x-api-key": "af46b22fcb404f39bf2703d831010401"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        collections = response.json().get('collections', [])
        
        if collections:
            # Shuffle collections to get random order
            random.shuffle(collections)
            
            # Iterate over collections to find one with a valid image_url
            for collection in collections:
                nft_image_url = collection.get('image_url')
                
                if nft_image_url:  # Check if image_url exists and is not empty
                    return JsonResponse({'nft_url': nft_image_url})
            
            # If no collections have a valid image_url
            return JsonResponse({'error': 'No NFT images found in collections'}, status=404)
        else:
            return JsonResponse({'error': 'No collections found'}, status=404)
    else:
        return JsonResponse({'error': 'Failed to fetch data from OpenSea'}, status=response.status_code)