__author__ = 'judyw'

from django import forms
from django.forms import ModelForm
from OMRS.models import UserProfile,Server
from django.contrib.auth.models import User


class serverParams(forms.Form):
    #need to specify the server details
    class Meta:
        model = Server
        fields = ('serverAddress','serverUsername','serverPassword')
        #serverAddress
        #encounterLocation
        #encounterType
        #defaultIdentifier

class UserForm (forms.ModelForm):
    password = forms.CharField(widget= forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','email','password','first_name','last_name')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website','middle_name','DOB','sex','country','organisation')

class serverForm(ModelForm):
    class Meta:
        model = Server
        #fields = '__all__'
        fields = ('user','serverAddress','serverUsername','serverPassword')

#form to upload file
class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )