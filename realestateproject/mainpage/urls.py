from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name='login'),
    path('forgetpassword/',views.forget_password, name='forgetpassword'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('welcome/',views.welcome, name='welcome'),
    path('buy/',views.buy, name='buy'),
    path('sell/',views.sell, name='sell'),
    path('payment/',views.payment, name='payment'),
]
