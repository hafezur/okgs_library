from django import forms 

from book.models import BookStoreModel

class BookStoreForm(forms.ModelForm):
    class Meta:
        model=BookStoreModel
        fields=['id','book_name','author','category','book_image']
    



from django import forms
from .models import UserRegistration
from django.core.exceptions import ValidationError

class RegistrationForm(forms.ModelForm):

    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': ' '}),
        label="Confirm Password"
    )

    class Meta:
        model = UserRegistration
        fields = [
            'first_name', 'last_name',
            'city', 'region', 'country',
            'present_address', 'permanent_address',
            'email', 'password'
        ]

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': ' '}),
            'last_name': forms.TextInput(attrs={'placeholder': ' '}),
            'city': forms.TextInput(attrs={'placeholder': ' '}),
            'region': forms.TextInput(attrs={'placeholder': ' '}),
            'country': forms.TextInput(attrs={'placeholder': ' '}),
            'present_address': forms.Textarea(attrs={'placeholder': ' ', 'rows': 3}),
            'permanent_address': forms.Textarea(attrs={'placeholder': ' ', 'rows': 3}),
            'email': forms.EmailInput(attrs={'placeholder': ' '}),
            'password': forms.PasswordInput(attrs={'placeholder': ' '}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise ValidationError("Passwords do not match!")

        return cleaned_data
