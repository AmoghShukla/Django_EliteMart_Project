from django.urls import path
from electronics import views  # ✅ Import the whole views module

urlpatterns = [
    path('', views.home, name='electronics'),  # ✅ Home page for electronics
]
