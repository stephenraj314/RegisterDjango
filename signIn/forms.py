from django import forms

class SigninForm(forms.Form):
    user_name = forms.CharField(label='User Name', max_length=100)
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    
