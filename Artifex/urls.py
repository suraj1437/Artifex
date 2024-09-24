"""
URL configuration for Artifex project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Nft_Analytics import views  # Import views from the Nft_Analytics app
from Nft_Analytics.views import generate_random_nft  # Correct import of views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.login_with_metamask, name='login_with_metamask'),
    path('fetch_crypto_data/', views.fetch_crypto_data, name='fetch_crypto_data'),
    path('trade/', views.tradepage, name='tradepage'),
    path('sidebar/', views.sidebar_page, name='sidebar_page'),
    path('generate-nft/', views.generate_nft_page, name='generate_nft_page'),
    path('generate-random-nft/', views.generate_random_nft, name='generate_random_nft'),
    path('generate_random_nft/', generate_random_nft, name='generate_random_nft'),
   
]




