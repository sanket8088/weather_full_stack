from django.shortcuts import render
from django.http import JsonResponse
import requests
import json

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def weather_city(request):
    try:
        return render(request, 'home.html')
    except Exception as e:
        
        return JsonResponse({"msg": e, "status": 400})

@csrf_exempt
def weather_info(request):
    data = request.POST
    print(data)
    ret = httpCall(request, data, "city/name/")
    ret=json.loads(ret)
    return JsonResponse({"link" : ret["data"] , "status_code" : 200})
   
def httpCall(request,data,url):
    try:
        apiUrl = "http://127.0.0.1:8000/"
        headers = {}
        url = apiUrl+url
        res = requests.post(url, data=data, files=request.FILES, headers=headers)
        return res.text
    except Exception as e:
        print("error-gen"+str(e))
        return "error !!"+str(e)
