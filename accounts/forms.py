from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Username",
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "Password",
    }))

    def clean(self):
        user = authenticate(username=self.cleaned_data.get("username"), password=self.cleaned_data.get("password"))
        if user is None:
            raise forms.ValidationError("Username or Password are Wrong", code="invalid_information")


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        widgets = {
            "first_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "First Name",
            }),
            "last_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Last Name",
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Email"
            })
        }
