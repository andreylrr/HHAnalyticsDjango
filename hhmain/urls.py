from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'hhmain'

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('index/', views.main_page, name='index'),
    path('login/', views.HHLogin.as_view(), name='login'),
    path('logout/', views.HHLogout.as_view(), name='logout'),
    path('contacts/', views.ContactsCreate.as_view(), name='contacts'),
    path('register/', views.UserRegister.as_view(), name='register'),
]
