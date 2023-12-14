from django.urls import path
from .views import home, personal

urlpatterns = [
    path('home/', home, name='home'),
    path('personal.html/', personal, name='personal'),
]
