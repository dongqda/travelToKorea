from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'maps/MainPage.html')

# detail page
def detailpage(request):
    return render(request, 'maps/DetailPage.html')

def map(request):
    return render(request, 'maps/map.html')

