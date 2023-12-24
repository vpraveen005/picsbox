from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('my_pictures/', views.my_pictures, name='my_pictures'),
    path('search/', views.search_pictures, name='search_pictures'),
    path('other_users_pictures/', views.other_users_pictures, name='other_users_pictures'),
    path('my_all_pictures/', views.my_all_pictures, name='my_all_pictures'),
]
