from django.shortcuts import render


def login_page(request):
    return render(request,'login.html')

def forget_password(request):
    return render(request,'forgetpassword.html')

def dashboard(request):
    return render(request,'dashboard.html')

def welcome(request):
    return render(request,'welcome.html')

def buy(request):
    return render(request,'buy.html')

def sell(request):
    return render(request,'sell.html')

def payment(request):
    return render(request,'payment.html')
# Create your views here.



