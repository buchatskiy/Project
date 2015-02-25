# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from loginsys.form import MyRegistrationForm
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context

def login(request):
    args = {}
    args.update(csrf(request))
    try:
        args['pieces'] = request.session['cart_pieces']
        args['summ'] = request.session['cart_sum']
    except:
        args['pieces'] = 0
        args['summ'] = 0
    args['username'] = auth.get_user(request).username
    if request.POST:
        username=request.POST.get('username','')
        password=request.POST.get('password','')
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            try:
                summ = 0
                for k in request.session['cart']:
                    k[5] = round(k[5]*0.95, 0)
                    k[6] = k[5]*k[4]
                    summ = summ+k[6]
            except:
                return redirect('/ALL/page/1/')
            request.session['cart'] = request.session['cart']
            request.session['cart_sum'] = summ
            return redirect('/ALL/page/1/')
        else:
            try:
                check_user = User.objects.get(username=username)
                args['login_error'] = 'Неверный пароль'
                args['username_old'] = username
                return render_to_response('login.html', args)
            except:
                args['login_error'] = 'Пользователь не найден'
                return render_to_response('login.html', args)
    else:
        return render_to_response('login.html', args)

def logout(request):
    auth.logout(request)
    return redirect('/ALL/page/1/')


def register(request):
    args = {}
    args.update(csrf(request))
    try:
        args['pieces'] = request.session['cart_pieces']
        args['summ'] = request.session['cart_sum']
    except:
        args['pieces'] = 0
        args['summ'] = 0
    args['form'] = MyRegistrationForm()
    if request.POST:
        newuser_form = MyRegistrationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username=newuser_form.cleaned_data['username'], password=newuser_form.cleaned_data['password2'])
            auth.login(request, newuser)
            """plaintext = get_template('email_register.txt')
            htmly = get_template('email_register.html')
            args['first_name'] = request.POST.get('first_name')
            args['last_name'] = request.POST.get('last_name')
            args['password'] = request.POST.get('password1')
            args['username_new'] = request.POST.get('username')
            d = Context(args)
            subject, from_email, to = 'Подтверждение успешной регистрации', 'xxxxxx@gmail.com', request.POST.get('email','')
            text_content = plaintext.render(d)
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()"""
            try:
                summ = 0
                for k in request.session['cart']:
                    k[5] = round(k[5]*0.95, 0)
                    k[6] = k[5]*k[4]
                    summ = summ+k[6]
            except:
                return redirect('/ALL/page/1/')
            request.session['cart'] = request.session['cart']
            request.session['cart_sum'] = summ
            return redirect('/ALL/page/1/')
        else:
            args['form']=newuser_form
    return render_to_response('register.html', args)
