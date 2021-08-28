from django.shortcuts import render
# Create your views here.
def home(request):
    return render(request,"home.html")

def howToGo(request):
    return render(request,"howToGo.html")

def sonjjangnan(request):
    return render(request,"sonjjangnan.html")

def introClass(request):
    return render(request,"introClass.html")