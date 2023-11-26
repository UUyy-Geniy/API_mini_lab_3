# API_mini_lab_3 Romanchuk Evgeniy 5030102/10201

-—
This application provides a simple api to find out some interesting information about cryptocurrencies.

## Application deployment and configuration

-—

### Requirements
- Python 3
- Postman
### Installation
1. Clone the repository:
```
git clone https://github.com/UUyy-Geniy/API_mini_lab_3
```
2. Install `django`:
```
pip install django
```
3. Install `requests`:
```
python -m pip install requests
```

## Run application

-—

To run the `django` application:
```
python manage.py runserver
```
And follow the link (Starting development server at http://127.0.0.1:8000/) to view the release

## Endpoints

-—
### Money + $
- **Endpoint:** `/`
- **Description:** Get 5 most popular cryptocurrencies and their prices

### Money + %(24h)
- **Endpoint:** `/money_with_change`
- **Description:** Get 7 most popular cryptocurrencies and their price_change_percentage_24h

### LOW AND HIGH
- **Endpoint:** `/money_with_high_and_low_price_24h`
- **Description:** Get the 5 most popular cryptocurrencies and their minimum and maximum values ​​in 24h


## Postman

-—
Postman workspace: https://www.postman.com/blue-comet-671848/workspace/team-workspace/request/31402705-2a2302a1-c1fd-4550-aab0-790e2ae048fb
