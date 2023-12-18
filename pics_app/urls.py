from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('my_pictures/', views.my_pictures, name='my_pictures'),
    path('search/', views.search_pictures, name='search_pictures'),
]
