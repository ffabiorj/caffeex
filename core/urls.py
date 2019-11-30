from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from core import views

urlpatterns = [
    path('stocks/', views.StockList.as_view()),
    path('stock/<int:pk>/', views.StockDetail.as_view()),
    path('coffeebags/', views.CoffeeBags.as_view()),
    path('coffeebag/<int:pk>/', views.CoffeeBagDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)