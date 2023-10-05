from django.contrib.auth.forms import UserCreationForm
from .models import RealSpaceUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model  = RealSpaceUser
        fields = ["email"]
