from django.urls import path
from grocery import views

urlpatterns = [
    path('', views.grocery , name='grocery'),  # Grocery Page
    
]