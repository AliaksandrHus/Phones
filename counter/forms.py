from django import forms


class LoginForm(forms.Form):

    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Введите логин'}))
    password = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Введите пароль'}))


class RegistrationForm(forms.Form):

    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Введите логин'}))
    email = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Введите почту'}))
    password = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Введите пароль'}))
    password_confirmation = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Повторите пароль'}))


