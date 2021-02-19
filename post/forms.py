from django import forms
from signUp.models import users
from django.core.exceptions import ValidationError

class PostForm(forms.Form):
    user_name = forms.CharField(label= 'User Name',max_length=100)
    post_title = forms.CharField(label='Post Title',max_length=100)
    post_desc = forms.CharField(label='Post Description',widget=forms.Textarea,max_length=1000)

    def clean_user_name(self):
        data = self.cleaned_data['user_name']
        if not users.objects.filter(user_name=data).first():

            raise ValidationError("Username Doesn't Exists")
        return users.objects.filter(user_name=data).first()
