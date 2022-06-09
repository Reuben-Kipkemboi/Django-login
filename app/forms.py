from django import forms
# django user model
from django.contrib.auth.models import User
# default django user creation form

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegisterForm(UserCreationForm):
    # fields we want to include and customize in our form
    first_name = forms.CharField(max_length=150,required=True,
    widget=forms.TextInput(attrs={'placeholder': 'Your First Name', 'class': 'form-control',}))
                                                       
    last_name = forms.CharField(max_length=150,required=True,
    widget=forms.TextInput(attrs={'placeholder': 'Your Last Name','class': 'form-control',}))
                                                              
    username = forms.CharField(max_length=100,required=True,
    widget=forms.TextInput(attrs={'placeholder': 'Provide your Username','class':'form-control', }))
                               
                                                            
    email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control',}))
                                                           
                             
                                                          
    password1 = forms.CharField(max_length=50,required=True,widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control','data-toggle': 'password', 'id':'password',})) 
                                                                         
    password2 = forms.CharField(max_length=50,required=True,
    widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'form-control','data-toggle': 'password','id': 'password',}))
                                
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username','email', 'password1', 'password2']


#login form
class UserLoginForm(AuthenticationForm):
    # fields we want to include and customize in our form
    username = forms.CharField(max_length=120,required=True,
    widget=forms.TextInput(attrs={'placeholder': 'Enter Your User Name', 'class': 'form-control',}))
                                                       
    password = forms.CharField(max_length=50,required=True,widget=forms.PasswordInput(attrs={'placeholder': 'User Password', 'class': 'form-control','data-toggle': 'password', 'id':'password',}))
      
    
    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']

