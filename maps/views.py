from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'maps/MainPage.html')

def base(request):
    return render(request, 'base.html')

# detail page
def detailpage(request):
    return render(request, 'maps/DetailPage.html')

