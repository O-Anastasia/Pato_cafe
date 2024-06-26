from django import forms
from django.contrib.auth.forms import User
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    """
    Class for login form
    """

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))

    def confirm_login_allowed(self, user) -> User:
        """
        Method for checking if a user is active
        """
        if not user.is_active:
            raise forms.ValidationError('Неактивный пользователь')
        return user

    def clean(self) -> dict:
        """
        Method for authentification users
        """
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user_cache = authenticate(self.request, username=username, password=password)
            if self.user_cache:
                self.confirm_login_allowed(self.user_cache)
            else:
                raise forms.ValidationError('Неверный логин или пароль')

        return self.cleaned_data

class RegisterForm(forms.ModelForm):
    """
    Class for user's registration
    """
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя пользователя'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Подтверждение пароля'}))

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self) -> str:
        """
        Method for checking if passwords match
        """
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Пароли не совпадают')
        return password2

    def save(self, commit=True) -> User:
        """
        Method for saving user in DataBase
        """
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user