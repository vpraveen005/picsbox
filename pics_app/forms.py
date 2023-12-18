from django import forms
from .models import Picture

class PictureUploadForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ['image', 'location']

    def save(self, commit=True, user=None):
        instance = super().save(commit=False)

        if user:
            instance.uploaded_by = user
        if commit:
            instance.save()
        return instance

class SearchForm(forms.Form):
    location = forms.CharField(required=False)
    upload_time = forms.CharField(required=False)

    def clean(self):
        cleaned_data = super().clean()
        location = cleaned_data.get('location')
        upload_time = cleaned_data.get('upload_time')

        if not location and not upload_time:
            raise forms.ValidationError("Please enter at least one search criteria.")

