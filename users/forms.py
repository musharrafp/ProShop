from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.forms import ModelForm, CharField, PasswordInput

from users.models import User


class UserForm(ModelForm):
    password = CharField(widget=PasswordInput())

    def clean_password(self):
        password = self.data.get('password')
        confirm_password = self.data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError('Password mos kelmadi')
        return make_password(password)

    class Meta:
        model = User
        fields = ('first_name', 'email', 'password')
