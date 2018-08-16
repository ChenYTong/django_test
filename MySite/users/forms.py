from django.contrib.auth.forms import UserCreationForm

from.models import User


class ResgisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')
