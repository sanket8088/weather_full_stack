
from django.urls import path, include
from weather import views as views

urlpatterns = [
    path('', views.weather_city, name="city_name"),
    path('city/name/', views.weather_info, name="city_name"),
    
]