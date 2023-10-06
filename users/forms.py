from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import RealSpaceUser


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(),
    )

    class Meta:
        model = RealSpaceUser
        fields = ["email"]
        field_classes = {'email': forms.EmailField}
