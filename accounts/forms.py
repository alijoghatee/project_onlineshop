from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

from .models import CustomUser


class CustomUserCreateForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['email', 'password']


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password']
