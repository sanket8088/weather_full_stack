from django.shortcuts import render
from django.http import JsonResponse
import requests
from bs4 import BeautifulSoup
from rest_framework.views import APIView

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from googlesearch import search 




class web_data(APIView):
    def post(self, request, format=None):
        print("llll")



class city_name(APIView):
    def post(self, request, format=None):
        try:
            data = request.POST
            print(data)
            city = list(data.keys())[0] + " weather"
            for j in search(city, tld="co.in", num=10, stop=1, pause=2): 
                link = j
            print(link)
            source = requests.get(link)
            print(source)
            plain = source.text
            soup=BeautifulSoup(plain)

            # return JsonResponse({"data" : link , "status_code" : 200})
        except Exception as e:
            print(e)
            return JsonResponse({ "status_code" : 400})
        
