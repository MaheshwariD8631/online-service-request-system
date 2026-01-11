from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('request/', views.add_request, name='add_request'),
    path('requests/', views.request_list, name='request_list'),
    path('request/<int:pk>/', views.request_detail, name='request_detail'),
]
