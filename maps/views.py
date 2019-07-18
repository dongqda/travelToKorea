from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'maps/MainPage.html')

def korea(request):
    return render(request, 'maps/korea.html')

# detail page
def detailpage(request):
    return render(request, 'maps/DetailPage.html')

