from django import forms
from .models import Video

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = '__all__'
        labels = {
            'MovieTitle': 'Movie Title',
            'Actor1Name': 'Actor 1 Name',
            'Actor2Name': 'Actor 2 Name',
            'DirectorName': 'Director Name',
            'MovieGenre': 'Movie Genre',
            'ReleaseYear': 'Release Year',
        }
