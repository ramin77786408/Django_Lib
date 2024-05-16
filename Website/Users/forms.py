from django import forms

class Signup(forms.Form):
    username         = forms.CharField(label="Username",max_length=30)
    first_name       = forms.CharField(label="First Name",max_length=30)
    last_name        = forms.CharField(label="Last Name",max_length=30)
    email            = forms.EmailField(label="Email")
    password         = forms.CharField(widget=forms.PasswordInput,label="Password")
    confirm_password = forms.CharField(widget=forms.PasswordInput,label="Confirm Password")

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password!= confirm_password:
            raise forms.ValidationError('Passwords do not match')
        return cleaned_data
    