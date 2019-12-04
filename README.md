[![Build Status](https://travis-ci.com/ffabiorj/caffeex.svg?branch=master)](https://travis-ci.com/ffabiorj/caffeex)
# API OF STOCK COFFEES
Development tools

* Django
* Django rest Framework

## How to run locally.

1. Clone the repository.
2. Enter in the folder
3. Create a enviroment with python 3.7.
4. Active the enviroment.
5. Install the dependencies.
6. Rename the file env_exemplo
7. Run the migrate
8. Create a superuser login
9. Run the project.
10. Access the link.
11. Enter with the login


```
git clone git@github.com:ffabiorj/caffeex.git
cd caffeex
python3 -m venv .venv
sourch .venv/bin/activate
pip install -r requirements.txt
mv .env_exemplo .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
http://127.0.0.1:8000/api/v1/stocks/
put the user and password
```

## Endpoints da api
To access the endpoints, you need to create a login.
```
http://127.0.0.1:8000/api/v1/stocks/
http://127.0.0.1:8000/api/v1/stock/<id>
http://127.0.0.1:8000/api/v1/coffeebags/
http://127.0.0.1:8000/api/v1/coffeebag/<id>

```

## To do a post method you will need:

```
Exemplo: Stock
{
    "name": "Farm",
    "origin_farm": "South",
    "quantity_bags_availible": 30,
    "stock_capacity": 50,
    "owner": user-id
}
Coffeebag
{
    "coffee_type": "Black",
    "origin": "Norte",
    "expirate_date": "2019-12-03",
    "quantity_bags": 10,
    "stock": stock-id   
}

```

## Execute tests
1. To test the api

```
python manage.py test
```

## I made deploy the app in the heroku.
1. You need login first: 
    - teste/eu12345678
2. Access the endpoints

```
https://caffeex-fabio.herokuapp.com/api/v1/stocks/
https://caffeex-fabio.herokuapp.com/api/v1/stock/1
https://caffeex-fabio.herokuapp.com/api/v1/coffeebags/
https://caffeex-fabio.herokuapp.com/api/v1/coffeebag/
```

### Obs. I will be keeping improve this app.
