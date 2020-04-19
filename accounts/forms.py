from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

from .models import User, YEAR, DEPT


class UserLoginForm(forms.Form):
    email = forms.EmailField()
    # username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None
        self.fields['email'].widget.attrs.update({'placeholder': 'Enter Email'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Enter Password'})

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        if email and password:
            self.user = authenticate(email=email, password=password)

            if self.user is None:
                raise forms.ValidationError("User Does Not Exist.")
            if not self.user.check_password(password):
                raise forms.ValidationError("Passwords does not match.")
            if not self.user.is_active:
                raise forms.ValidationError("Account is not active yet. Please check your email and confirm your email address")

        return super(UserLoginForm, self).clean(*args, **kwargs)

    def get_user(self):
        return self.user


class UserRegistrationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].icon = '<span class="input-field-icon"><i class="fas fa-envelope"></i></span>'
        self.fields['first_name'].widget.attrs.update({'placeholder': 'Enter First Name'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Enter Last Name'})
        self.fields['username'].widget.attrs.update({'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email'})
        self.fields['whatsApp_number'].widget.attrs.update({'placeholder': 'Enter your WhatsApp number'})
        self.fields['contact_number'].widget.attrs.update({'placeholder': 'Your contact number'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Enter password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Again password'})

    class Meta:
        model = User
        fields = ("username",
                  "first_name",
                  "last_name",
                  "email",
                  "password1",
                  "password2",
                  "contact_number",
                  "whatsApp_number")

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email:
            raise forms.ValidationError('Enter valid email')
        return email

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    
class ProfileUpdateForm(forms.ModelForm):

    graduation_year_of_BTech = forms.ChoiceField(choices=YEAR, required=False)
    your_deparment_of_study = forms.ChoiceField(choices=DEPT, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs.update({'placeholder': 'Enter first name'})
        self.fields["last_name"].widget.attrs.update({'placeholder': 'Enter last name'})
        self.fields["parent_name"].widget.attrs.update({'placeholder': 'Enter the name of your guardian'})
        self.fields["whatsApp_number"].widget.attrs.update({'placeholder': 'Enter your WhatsApp number'})
        self.fields["address"].widget.attrs.update({'placeholder': 'Please mention your address / locality in brief'})
        self.fields["name_of_your_college"].widget.attrs.update({'placeholder': 'Name of the College / University you are admitted to'})
        self.fields["contact_number"].widget.attrs.update({'placeholder': 'Your contact number'})


    class Meta:
        model = User
        fields = ["first_name",
            "last_name",
            "parent_name",
            "contact_number", 
            "whatsApp_number", 
            "address", 
            "name_of_your_college", 
            "graduation_year_of_BTech", 
            "your_deparment_of_study",
            "average_SGPA_till_last_published_semester",  
            "class_12_mark_in_percentage"]
