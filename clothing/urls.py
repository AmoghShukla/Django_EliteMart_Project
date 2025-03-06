from django.urls import path
from clothing import views

urlpatterns = [
    path('', views.clothing, name='clothing'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('', views.fashion, name='home'),  
    path('about/', views.about, name='about'),  
    path('contact/', views.contact, name='contact'),  
    path('home/', views.home_flipkart, name='home_flipkart'),  
]
