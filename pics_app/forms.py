from django import forms
from .models import Pictures

class PictureUploadForm(forms.ModelForm):
    class Meta:
        model = Pictures
        fields = ['image', 'location']
