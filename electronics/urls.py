from django.urls import path
from clothing import views

urlpatterns = [
    path('clothing/', views.clothing, name='clothing'),
]