from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import UserLoginActivity
from django.contrib.auth.forms import User as auth_User

class UserCreateForm(UserCreationForm):
    """ Builtin User signup form   """
    class Meta:
        fields = ('username','email','password1','password2')
        model  = get_user_model()

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label='Display Name'
        self.fields['email'].label='Email Address'


class UserForm(forms.ModelForm):
    """ Activity periods Form  """
    class Meta:
        model = UserLoginActivity
        fields='__all__'

    def save(self,request):
        request.username=self.real_name  

class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)

    def validate(self,attrs):
        credentials={
            self.username:attrs.get(self.username),
            'password':attrs.get('password')
        }

