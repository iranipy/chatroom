from django import forms

from .models import PrivateRoom


class PrivateRoomCreationForm(forms.ModelForm):
    class Meta:
        model = PrivateRoom
        fields = ['name', 'password', 'description', 'capacity']


class EnterPrivateRoom(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)
