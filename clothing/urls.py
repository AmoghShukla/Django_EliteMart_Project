from django.urls import path
from clothing import views

urlpatterns = [
    path('', views.clothing, name='clothing'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('', views.fashion, name='home'),  # Homepage (Fashion)
    path('about/', views.about, name='about'),  # About Page
    path('contact/', views.contact, name='contact'),  # Contact Page
    path('home/', views.home_flipkart, name='home_flipkart'),  # Home Page
]
