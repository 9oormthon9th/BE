from django.shortcuts import render
from django.http import HttpResponse
#import requests

# Create your views here.

def index(request):
    return render(request, 'kakaopai/map.html')

'''headers = {
    "Authorization" : "KakaoAK 1a98ba4401035233ab63c049917b079d"
}

response = requests.get("https://dapi.kakao.com/v2/local/search/address.json", headers=headers")
                        
'''