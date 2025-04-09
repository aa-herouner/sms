# from django import forms
# from .models import UserAuthentication
# class UserLoginForm(forms.Form):
#     class meta:
#         models = UserAuthentication

#     username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}))

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .models import CustomUser, CustomUserManager

class CustomLoginForm(AuthenticationForm):
        username = forms.CharField(
            max_length=30,
            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
        )
        password = forms.CharField(
            widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
        )

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = "Enter a strong password."
        self.fields['password2'].help_text = "Enter the same password as above, for verification."


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_admin')

