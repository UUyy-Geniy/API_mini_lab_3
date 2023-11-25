from django.urls import path
from . import views

urlpatterns = [
    path('',views.money_with_price, name='money_with_price'),
    path('money_with_change', views.money_with_change, name='money_with_change'),
    path('money_with_high_and_low_price_24h', views.money_with_high_and_low_price_24h, name='money_with_high_and_low_price_24h'),
]