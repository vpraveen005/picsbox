from django.shortcuts import render, redirect, get_object_or_404
from .models import Picture
from .forms import PictureUploadForm, SearchForm
from django.contrib.auth.decorators import login_required
from datetime import datetime


def home(request):
    context = {
        "home_text": "Photo Gallery"
    }
    return render(request, 'pics_app/home.html', context)

@login_required
def my_pictures(request):
    if request.method == 'POST':
        form = PictureUploadForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.uploaded_by = request.user
            form.save(user=request.user)
    else:
        form = PictureUploadForm()
    pictures = Picture.objects.all()
    return render(request, 'pics_app/my_pictures.html', {'form': form, 'pictures': pictures})

# @login_required
# def search_pictures(request):
#     location = request.GET.get('location', '')
#     upload_time = request.GET.get('upload_time', '')
#
#     pictures = Picture.objects.filter(location__icontains=location, upload_time__icontains=upload_time)
#
#     return render(request, 'pics_app/search_pictures.html', {'pictures': pictures})

@login_required
def search_pictures(request):
    form = SearchForm(request.GET)

    if form.is_valid():
        location = form.cleaned_data.get('location', '')
        date_query = form.cleaned_data.get('upload_time', '')
        pictures = Picture.objects.all()
        if location:
            pictures = pictures.filter(location__icontains=location)
        if date_query:
            try:
                date_query = datetime.strptime(date_query, '%b. %d, %Y')

                year = date_query.year
                month = date_query.month
                day = date_query.day

                pictures = pictures.filter(upload_time__year=year, upload_time__month=month, upload_time__day=day)
            except ValueError:
                pass

        return render(request, 'pics_app/search_pictures.html', {'pictures': pictures, 'form': form})
    else:
        return render(request, 'pics_app/my_pictures.html', {'form': form})
