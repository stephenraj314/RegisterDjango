from django import forms

class SignupForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    user_name = forms.CharField(label='User Name', max_length=100)
    email = forms.EmailField()
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    Repassword = forms.CharField(label='RePassword',widget=forms.PasswordInput)
