
from django.urls import path, include
from django.conf.urls import url
from web_scrap import views as views

urlpatterns = [
    url(r'web/scrap/$', views.web_data.as_view(), name="web_data"),
    url(r'city/name/$', views.city_name.as_view(), name="city_name"),

]