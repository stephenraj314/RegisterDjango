from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
import re


def regex_password(value):
    pat="^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$"
    if bool(re.match(pat,value))==False:
        raise ValidationError("Match The Passwoed Criteria")
class SignupForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    user_name = forms.CharField(label='User Name', max_length=100)
    email = forms.EmailField()
    password = forms.CharField(label='Password',widget=forms.PasswordInput,validators=[regex_password])
    Repassword = forms.CharField(label='RePassword',widget=forms.PasswordInput)


'''
def validate_even(value):
if value  != 0:
    raise ValidationError(
        _('%(value)s is not an even number'),
        params={'value': value},
    )
'''
