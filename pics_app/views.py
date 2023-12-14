from django.shortcuts import render
from .models import Pictures
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    pictures = Pictures.objects.all()
    return render(request, 'pics_app/home.html', {'pictures': pictures})

@login_required
def personal(request):
    user_pictures = Pictures.objects.filter(user=request.user)
    return render(request, 'pics_app/personal.html', {'user_pictures': user_pictures})
