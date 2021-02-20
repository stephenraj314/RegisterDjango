from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from .models import users
import re
import bcrypt




class SignupForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    user_name = forms.CharField(label='User Name', max_length=100)
    email = forms.EmailField()
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    Repassword = forms.CharField(label='RePassword',widget=forms.PasswordInput)

    def clean_Repassword(self):
        try:
            password = self.cleaned_data['password']
        except:
            raise forms.ValidationError("Match The Passwoed Criteria /n 8 charcters /n one alpahet one digit on special charactr")
        re_password = self.cleaned_data['Repassword']
        if password != re_password  :
            raise forms.ValidationError("password doesn't Match")
        return re_password

    def clean_password(self):
        data = self.cleaned_data['password']
        pat="^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$"
        if bool(re.match(pat,data))==False:
            raise ValidationError("Match The Password Criteria")
        return data

    def clean_user_name(self):
        data = self.cleaned_data['user_name']
        if users.objects.filter(user_name=data).first():
            raise ValidationError("Username Already Exists")
        return data






'''
def validate_even(value):
if value  != 0:
    raise ValidationError(
        _('%(value)s is not an even number'),
        params={'value': value},
    )
'''
