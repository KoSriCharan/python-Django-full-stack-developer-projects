from django import forms
from django.core import validators
from basicapp.models import User


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, 
                              widget=forms.HiddenInput,
                              validators=[validators.MaxLengthValidator(0)])
    
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        if not email.endswith('edu'):
            raise forms.ValidationError("Email has to end with .edu")

class NewUser(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'