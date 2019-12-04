from django.contrib import admin
from core.models import Stock, CoffeeBag


admin.site.register([Stock, CoffeeBag])
