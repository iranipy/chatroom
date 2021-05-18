from django import forms

from .models import PrivateRoom


class PrivateRoomCreationForm(forms.ModelForm):
    class Meta:
        model = PrivateRoom
        fields = ['name', 'password', 'slug', 'description', 'capacity']



