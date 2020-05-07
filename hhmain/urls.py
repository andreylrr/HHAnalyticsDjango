from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'hhmain'

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('index/', views.main_page, name='index'),
    path('login/', views.login, name='login'),
    path('contacts/', views.ContactsCreate.as_view(), name='contacts'),
    path('forgot-password/', views.forgot_password, name='forgot-password'),
    path('register/', views.UserRegister.as_view(), name='register'),
]
