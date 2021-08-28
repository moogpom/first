from django.contrib.auth.forms import UserCreationForm,UserChangeForm,get_user_model
from .models import SonUser

class SignUpForm(UserCreationForm):
    class Meta:
        model = SonUser
        fields=['username','password1','password2','dog','like','introduce']

class SonUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = [ 'dog','like','introduce']