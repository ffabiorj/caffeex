from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from core import views

urlpatterns = [
    path('stocks/', views.StockList.as_view(), name='stocks'),
    path('stock/<int:pk>/', views.StockDetail.as_view(), name='stock'),
    path('coffeebags/', views.CoffeeBags.as_view(), name='coffeebags'),
    path('coffeebag/<int:pk>/', views.CoffeeBagDetail.as_view(), name='coffeebag'),
]

urlpatterns = format_suffix_patterns(urlpatterns)