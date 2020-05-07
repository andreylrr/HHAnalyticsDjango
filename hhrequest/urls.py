from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'hhrequest'

urlpatterns = [
    path('request', views.RequestCreate.as_view(), name='request' ),
    path('history', views.RequestsListView.as_view(), name='history'),
    path('detail_request/<int:pk>/', views.RequestDetailView.as_view(), name='detail_request'),
]
