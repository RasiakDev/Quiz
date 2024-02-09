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
    question = forms.CharField(widget=forms.Textarea(attrs={"rows":"5"}))
    option1 = forms.CharField(max_length=100)
    option2 = forms.CharField(max_length=100)
    option3 = forms.CharField(max_length=100, required=False)
    option4 = forms.CharField(max_length=100, required=False)
    correct = forms.CharField(max_length=100)
    category = forms.ModelChoiceField(Kategori.objects.all())
    
  
