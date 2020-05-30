from django import forms
from django.core import validators
from django.contrib.auth.models import User
from myapp.models import *

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ['mprofile',]
class AddItemForm(forms.ModelForm):
    class Meta():
        model = customItem
        exclude = ["pub_date",]
class AddCommentForm(forms.ModelForm):
    class Meta():
        model = Comments
        fields = ["text",]