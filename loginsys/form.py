# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User   # fill in custom user info then save it
from django.contrib.auth.forms import UserCreationForm

class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required = True, label=("E-mail*"))
    first_name = forms.CharField(required = False, label=("Имя"))
    last_name = forms.CharField(required = False, label=("Фамилия"))
    username = forms.CharField(required = True, label=("Логин*"), help_text=('Обязательное поле. Не более 30 символов. Только буквы, цифры и символы @/./+/-/_.'))
    password1 = forms.CharField(required = True, label=("Пароль*:"), widget=forms.PasswordInput)
    password2 = forms.CharField(required = True, label=("Подтверждение пароля*:"), help_text=('Введите тот же пароль, что и выше, для подтверждения.'), widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')

    def save(self, commit = True):
        user = super(MyRegistrationForm, self).save(commit = False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        if len(password) < 4:
            raise forms.ValidationError('Пароль должен состоять хотя бы из 4 символов')
        return password


    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError('Пользователь с таким e-mail уже существует, ввойдите под своим логином.')
        return email