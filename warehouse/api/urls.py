from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.CreateOrder.as_view(), name='create'),
]
