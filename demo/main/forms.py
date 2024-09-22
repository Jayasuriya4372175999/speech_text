from django import forms
from .models import Patient_details
from django.core.validators import RegexValidator

class PatientDetailsForm(forms.ModelForm):
    # Add custom widgets and validators for the fields if needed

    phone_number = forms.CharField(
        max_length=15,
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")],
        widget=forms.TextInput(attrs={'placeholder': 'Phone Number'})
    )
    
    dob = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%m/%d/%Y', '%Y-%m-%d'],  # Accepting MM/DD/YYYY and YYYY-MM-DD formats
    )

    email_address = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Email Address'})
    )

    class Meta:
        model = Patient_details
        fields = ['first_name', 'last_name', 'father_name', 'age', 'sex', 'dob', 'phone_number', 'email_address']
        widgets = {
            'sex': forms.Select(attrs={'class': 'form-select'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'father_name': forms.TextInput(attrs={'placeholder': 'Father\'s Name'}),
            'age': forms.NumberInput(attrs={'placeholder': 'Age'}),
        }
