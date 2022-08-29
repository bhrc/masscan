from django import forms
from django.contrib.auth.models import User

class UpdateUserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خود را وارد کنید'}))
    last_name = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خانوادگی خود را وارد کنید'}))
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'dir': 'ltr', 'readonly': 'true', 'placeholder': 'نام کاربری'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'dir': 'ltr', 'placeholder': 'ایمیل خود را وارد کنید'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
