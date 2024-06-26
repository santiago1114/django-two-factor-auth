from django import forms
from django.utils.translation import gettext_lazy as _

from two_factor.forms import (
    AuthenticationTokenForm as BaseAuthenticationTokenForm,
    DeviceValidationForm as BaseValidationForm,
)


class EmailForm(forms.Form):
    email = forms.EmailField(label=_("Email address"))
    email.widget.attrs.update({'class': 'form-control'})

    def __init__(self, **kwargs):
        kwargs.pop('device', None)
        super().__init__(**kwargs)


class DeviceValidationForm(BaseValidationForm):
    token = forms.CharField(label=_("Token"))
    token.widget.attrs.update({'autofocus': 'autofocus',
                               'autocomplete': 'one-time-code',
                               'class': 'form-control'})
    idempotent = False  # Once validated, the token is cleared.


class AuthenticationTokenForm(BaseAuthenticationTokenForm):
    def _chosen_device(self, user):
        return self.initial_device
