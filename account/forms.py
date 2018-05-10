from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile


class RegisterForm(UserCreationForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password. Extends the UserCreationForm."""
    first_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email',
                  'password1', 'password2')


class ProfileVerificationForm(forms.ModelForm):
    """A form for updating the user Profile in order to verified account."""
    disabled_fields = ('date_of_birth', 'document_country_of_issue',
                  'document_series', 'id_document_expiration_date',
                  'document_scan')
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'document_country_of_issue',
                  'document_series', 'id_document_expiration_date',
                  'phone_number', 'document_scan')

    def __init__(self, *args, **kwargs):
        super(ProfileVerificationForm, self).__init__(*args, **kwargs)
        for field in self.disabled_fields:
            self.fields[field].disabled = True