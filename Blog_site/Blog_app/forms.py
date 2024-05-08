from django import forms
from . models import Blog
from django.contrib.auth.models import User         ############ DEFAULT USER MODEL
from django.contrib.auth.forms import UserCreationForm      ############## DEFAULT USERCREATION FORM

##################   USER REGISTER FORM  ###########################

class UserRegisterForm(UserCreationForm):
    model=User
    fields='__all__'

#################  BLOG POST FORM  #################################
    
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'img', 'description'] 