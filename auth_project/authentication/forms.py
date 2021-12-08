
from django import forms
from authentication.models import MyUser
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm,PasswordResetForm

class MyUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "First Name",
                "name":"first_name",
                "class":"input100"
            }
        ))
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Last Name",
                "name":"last_name",
                "class":"input100",
                "blank":True
            }
        ))
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",
                "class":"input100",
                "name":"username"
            }
        ))
    mobile_number = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Mobile",
                "class":"input100",
                "name":"mobile_number"
            }
        ),required=False)
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "email",
                "name":"email",
                "class":"input100",
                "required":True,
                "unique":True
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",
                "class":"input100",
                "name":"pass"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Confirm Password",
                "class":"input100",
                "name":"pass"
            }
        ))
    class Meta(UserCreationForm):
        model=MyUser
        fields = ('username', 'mobile_number','email','first_name','last_name')

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",
                "class":"input100",
                "name":"username"
            }
        ))
    # email = forms.EmailField(
    #     widget=forms.EmailInput(
    #         attrs={
    #             "placeholder" : "email",
    #             "name":"email",
    #             "class":"input100"
    #         }
    #     ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",
                "class":"input100",
                "name":"pass"
            }
        ))
class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Old Password",
                "class":"input100",
                 "name":"pass"
            }
        ))
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Enter new password",
                "class":"input100",
                 "name":"pass"
            }
        ))
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Confirm password",
                "class":"input100",
                 "name":"pass"
            }
        ))
# class MyPasswordResetForm(PasswordResetForm):
class MyPasswordResetForm(forms.Form):

    # email = forms.CharField(
    # widget=forms.EmailInput(
    #     attrs={
    #         "placeholder" : "Enter email",        
    #          "class":"input100",        
    #             "name":"email"
    #     }
    # ))
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",
                "class":"input100",
                "name":"username"
            }
        ))
class SetPasswordForm(forms.Form):
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Enter new password",
                "class":"input100",
                 "name":"pass"
            }
        ))
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Confirm password",
                "class":"input100",
                 "name":"pass"
            }
        ))
