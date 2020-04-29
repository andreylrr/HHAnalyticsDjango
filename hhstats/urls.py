from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'hhstats'

urlpatterns = [
    path('request', views.StatsRequestCreate.as_view(), name='stats-request' ),
]
