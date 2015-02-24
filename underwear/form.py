# -*- coding: utf-8 -*-
from django import forms
from underwear.models import Purchase


class MyCartForm1(forms.ModelForm):
    purchase_number = forms.CharField(widget=forms.HiddenInput())
    first_name = forms.CharField(required=True, label="Имя")
    last_name = forms.CharField(required=True, label="Фамилия")
    phone_number = forms.RegexField(regex=r'^\+?1?\d{12}$', error_message = "Номер телефона должен быть введен в формате: '+380xxxxxxxx'", label="Телефон", initial='+380')
    city = forms.CharField(required=True, label="Город")
    totalprice = forms.DecimalField(widget=forms.HiddenInput())
    underwear = forms.CharField(widget=forms.HiddenInput())
    post_office = forms.CharField(required=True, label="Номер отделения Новой Почты")
    divisions = forms.ChoiceField(label="", choices=(("a", "Доставка наложенным платежом"),("b", "100% оплата на карту Приват Банка*"),), widget=forms.RadioSelect(),)

    class Meta:
        model = Purchase
        fields = ('purchase_number', 'first_name', 'last_name', 'phone_number', 'city', 'post_office', 'divisions', 'totalprice', 'underwear',)


class MyCartForm2(forms.ModelForm):
    purchase_number = forms.CharField(widget=forms.HiddenInput())
    first_name = forms.CharField(required=True, label="Имя*")
    phone_number = forms.RegexField(regex=r'^\+?1?\d{12}$', error_message = "Номер телефона должен быть введен в формате: '+380xxxxxxxx'", label="Телефон*", initial='+380')
    city = forms.CharField(required=True, label="Адрес доставки*")
    comment = forms.CharField(required=False, label="Комментарий", widget=forms.Textarea)
    totalprice = forms.DecimalField(widget=forms.HiddenInput())
    underwear = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = Purchase
        fields = ('purchase_number', 'first_name','phone_number', 'city', 'comment', 'totalprice', 'underwear',)