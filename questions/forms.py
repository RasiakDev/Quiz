from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Pyetje, Kategori

# authentication/forms.py
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','email','first_name','last_name', 'password1','password2'] 

class QuestionForm(forms.Form):
    question = forms.CharField(widget=forms.Textarea(attrs={"rows":"5"}),label="Pyetja")
    option1 = forms.CharField(max_length=100,label="Optioni 1")
    option2 = forms.CharField(max_length=100,label="Optioni 2")
    option3 = forms.CharField(max_length=100, required=False,label="Optioni 3")
    option4 = forms.CharField(max_length=100, required=False,label="Opsioni 4")
    correct = forms.CharField(max_length=100,label="Pergjigja e sakte")
    category = forms.ModelChoiceField(Kategori.objects.all(),label="Kategoria")
    
  
