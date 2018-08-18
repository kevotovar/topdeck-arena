from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

from crispy_forms.layout import Submit

from core.forms import BaseForm

class SignUpForm(UserCreationForm, BaseForm):
    name = forms.CharField(max_length=30, required=False, label=_('name'))

    class Meta:
        model = get_user_model()
        fields = ('email', 'name', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Registrarse'))
