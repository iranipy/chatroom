from django import forms

from .models import PrivateRoom


class PrivateRoomCreationForm(forms.ModelForm):
    class Meta:
        model = PrivateRoom
        fields = ['name', 'password', 'description', 'capacity']


class EnterPrivateRoom(forms.Form):
    roomname = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
