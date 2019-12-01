[![Build Status](https://travis-ci.com/ffabiorj/caffeex.svg?branch=master)](https://travis-ci.com/ffabiorj/caffeex)
# API OF STOCK
Development tools

* Django
* Django rest Framework

## Como executar o api localmente.

1. Clone the repository.
2. Enter in the pholder
2. create a environment with python 3.7.
3. Active the environment.
4. Install the dependencies.
5. Run the migrate
8. Run the project.
7. Access the link.


```
git clone git@github.com:ffabiorj/caffeex.git
cd caffeex
python3 -m venv .venv
sourch .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
http://127.0.0.1:8000/api/v1/stocks/
```

## Endpoints da api
To access the endpoints, you need to create a login.
```
http://127.0.0.1:8000/api/v1/stocks/
http://127.0.0.1:8000/api/v1/stock/<id>
http://127.0.0.1:8000/api/v1/coffeebags/
http://127.0.0.1:8000/api/v1/coffeebag/<id>

```

## Execute tests
1. Realizar setup dos test

```
python manage.py test
```
