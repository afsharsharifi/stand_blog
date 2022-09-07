from django import forms
from . import models


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = models.Message
        exclude = ("is_read",)
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your title...",
            }),
            "text": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Enter your message...",
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your email..."
            })
        }
