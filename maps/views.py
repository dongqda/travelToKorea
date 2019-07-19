from django.shortcuts import render
import urllib.request
import json
from pprint import pprint

# Create your views here.

def main(request):
    ServiceKey = "tG2pbhauvACu6IO20lRl4NIY5qDcRrFnl21s57G6XgwovyquyiFquhZgoE%2FBmG930wyBEyxx4pNZEyxzt8%2Brvg%3D%3D"
    url = "http://api.visitkorea.or.kr/openapi/service/rest/KorService/"
    key = "?ServiceKey=" + ServiceKey
    get = "areaCode"
    option = "&numOfRows=17&pageNo=1&MobileOS=AND&MobileApp=travel5&_type=json"
    url_ = url + get + key + option

    request_ = urllib.request.Request(url_)
    response = urllib.request.urlopen(request_)
    rescode = response.getcode()

    if (rescode == 200):
        response_body = response.read()
        dict = json.loads(response_body.decode('utf-8'))
        pprint(dict)
        value = dict['response']['body']['items']['item']
        context = {'value': value }
        return render(request, 'maps/MainPage.html', context)
    else:
        print("Error Code:" + rescode)
        return render(request, 'maps/MainPage.html')



 def korea(request):
    return render(request, 'maps/korea.html')

# detail page
def detailpage(request):
    return render(request, 'maps/DetailPage.html')

def map(request):
    return render(request, 'maps/map.html')
