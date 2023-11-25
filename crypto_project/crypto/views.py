from django.shortcuts import render
import requests

def get_crypto_data_with_price():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': 'usd', 
        'order': 'market_cap_desc',
        'per_page': 5,
        'page': 1,
    }
    response = requests.get(url, params=params)
    dict = {}
    if response.status_code == 200:
        data = response.json()
        for crypto in data:
            name = crypto['name']
            price = crypto['current_price']
            dict[name] = price
        return dict
    else:
        print(f"Ошибка при запросе: {response.status_code}")


def get_crypto_data_with_price_change_24h():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': 'usd', 
        'order': 'market_cap_desc',
        'per_page': 7,
        'page': 1,
        'price_change_percentage': '24h',
    }
    response = requests.get(url, params=params)
    dict = {}
    if response.status_code == 200:
        data = response.json()
        for crypto in data:
            name = crypto['name']
            price_change = crypto['price_change_percentage_24h']
            dict[name] = price_change
        return dict
    else:
        print(f"Ошибка при запросе: {response.status_code}")


def find_most_and_least_expensive_currency():
    currency_dict = get_crypto_data_with_price()
    if not currency_dict:
        return None, None
    max_currency = max(currency_dict, key=currency_dict.get)
    max_price = currency_dict[max_currency]
    min_currency = min(currency_dict, key=currency_dict.get)
    min_price = currency_dict[min_currency]

    return max_currency, max_price, min_currency, min_price


def get_crypto_data_with_high_and_low_price_24h():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': 'usd', 
        'order': 'market_cap_desc',
        'per_page': 5,
        'page': 1,
    }
    response = requests.get(url, params=params)
    dict = {}
    if response.status_code == 200:
        data = response.json()
        for crypto in data:
            el_data=[]
            name = crypto['name']
            high = crypto['high_24h']
            low = crypto['low_24h']
            el_data.append(high)
            el_data.append(low)
            dict[name] = el_data
        return dict
    else:
        print(f"Ошибка при запросе: {response.status_code}")


def money_with_change(request):
    return render(request, 'crypto/money_with_change.html',
                   {'title':'Валюты и изменение за сутки', 'res': get_crypto_data_with_price_change_24h()})

def money_with_price(request):
    return render(request, 'crypto/money_with_price.html',
                   {'title':'Стоимость валют', 'res_price': get_crypto_data_with_price()})

def money_with_high_and_low_price_24h(request):
    return render(request, 'crypto/money_with_high_and_low_price_24h.html',
                   {'title':'Минимум и максимум стоимость валюты за сутки', 'res': get_crypto_data_with_high_and_low_price_24h()})