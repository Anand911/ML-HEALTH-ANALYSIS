
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import  User
from django import forms

register_styles={'class':'field'}
class CreateUserForm(UserCreationForm):
    email=forms.EmailField()
    
    class Meta:
        model=User
        fields=['username','email','password1','password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs["placeholder"]='username'
        

