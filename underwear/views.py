# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect
from underwear.models import Series, Underwear, Purchase
from django.contrib import auth
from django.core.paginator import Paginator
from django.core.context_processors import csrf
from underwear.form import MyCartForm1, MyCartForm2
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
import datetime
from django.core.validators import validate_email
from django.db.models import Q


def main(request, page_number='1', current_series='ALL'):
    args = {}
    request.session['size'] = request.session.get('size', 'M')
    if request.session['size'] == 'L':
        all_underwear = Underwear.objects.order_by('-availableL')
    else:
        if request.session['size'] == 'XL':
            all_underwear = Underwear.objects.order_by('-availableXL')
        else:
            all_underwear = Underwear.objects.all()
    request.session['current_series'] = current_series
    if current_series != 'ALL':
        all_underwear = all_underwear.filter(Q(series=Series.objects.get(name=current_series)) | Q(series=Series.objects.get(name='Package')))
    all_series = Series.objects.all()
    current_page = Paginator(all_underwear, 6)
    s = dict()
    for p in all_series:
            s[p.id] = [round(p.price*0.95, 0), round(p.price, 0)]
    try:
        args['pieces'] = request.session['cart_pieces']
        args['summ'] = request.session['cart_sum']
    except:
        args['pieces'] = 0
        args['summ'] = 0

        args['current_series'] = 'ALL'
    args['current_series'] = current_series
    args['text'] = current_page.page(page_number)
    args['username'] = auth.get_user(request).username
    args['series'] = s
    args['current_page'] = request.get_full_path()
    args['size'] = request.session['size']
    return render_to_response('base.html', args)


def size(request, newsize):
    request.session['size'] = newsize
    try:
        current_series = request.session['current_series']
    except:
        current_series = 'ALL'
        request.session['current_series'] = 'ALL'
    return redirect('/'+current_series+'/page/1/')

def buy(request):
    if 'price' in request.GET:
        price = request.GET['price']
        if 'underwear' in request.GET:
            underwear = request.GET['underwear']
            if 'size' in request.GET:
                size = request.GET['size']
                series = request.GET['series']
                try:
                    color = request.GET['color']
                except:
                    color = ""
                b = 0
                pieces = 0
                summ = 0
                all_series = Series.objects.all()
                for p in all_series:
                    if p.id == int(str(series)): series_new = p.name
                try:
                    for k in request.session['cart']:
                        pieces = pieces+k[4]
                        summ = summ+k[6]
                        if k[3] == underwear and k[2] == size:
                            b = 1
                            k[6] = k[6]+float(str(price).replace(',','.'))
                            summ = summ+float(str(price).replace(',','.'))
                            k[4] = k[4]+1
                            pieces = pieces+1
                    if b == 0:
                        request.session['cart_id'] += 1
                        request.session['cart_id'] = request.session['cart_id']
                        request.session['cart'].append([request.session['cart_id'], series_new, size, underwear, 1, float(str(price).replace(',','.')), float(str(price).replace(',','.')), color])
                        summ=summ+float(str(price).replace(',','.'))
                        pieces=pieces+1
                except:
                    request.session['cart_id'] = 1
                    request.session['cart']=[[request.session['cart_id'], series_new, size, underwear, 1, float(str(price).replace(',','.')), float(str(price).replace(',','.')), color]]
                    summ = summ+float(str(price).replace(',','.'))
                    pieces = pieces+1

                request.session['cart'] = request.session['cart']
                request.session['cart_pieces'] = pieces
                request.session['cart_sum'] = summ
                return redirect(request.GET['current_page'])

def cart(request, delivery):
    args = {}
    args.update(csrf(request))
    try:
        args['pieces'] = request.session['cart_pieces']
        args['summ'] = request.session['cart_sum']
    except:
        args['pieces'] = 0
        args['summ'] = 0
    try:
        args['cart'] = request.session['cart']
    except:
        args['cart'] = ""
    args['username'] = auth.get_user(request).username
    now = datetime.date.today()
    month_purchase = Purchase.objects.all()
    new_purchase_number = 0
    for date_purchase in month_purchase:
        q=str(date_purchase.date).split('-')
        if int(q[0])==now.year and int(q[1])==now.month: new_purchase_number = new_purchase_number+1
    new_purchase_number+=1
    args['new_purchase_number'] = str(new_purchase_number)+"/"+str(now.month)
    try:
        first_name = auth.get_user(request).first_name
        last_name = auth.get_user(request).last_name
    except:
        first_name = ""
        last_name = ""
    if delivery == 1: args['form'] = MyCartForm1(initial={'totalprice': float(request.session['cart_sum']), 'underwear':";".join(str(k[3])+str(k[2])+' '+str(k[7].encode('utf-8'))+" "+str(k[4])+"шт"  for k in request.session['cart']), 'purchase_number':str(new_purchase_number)+"/"+str(now.month), 'first_name': first_name, 'last_name': last_name})
    if delivery == 2: args['form'] = MyCartForm2(initial={'totalprice': float(request.session['cart_sum']), 'underwear':";".join(str(k[3])+str(k[2])+' '+str(k[7].encode('utf-8'))+" "+str(k[4])+"шт"  for k in request.session['cart']), 'purchase_number':str(new_purchase_number)+"/"+str(now.month), 'first_name': first_name, 'last_name': last_name})
    args['delivery'] = delivery
    if delivery == 1 and request.session['cart_sum'] == 0: return redirect('/', args)
    if delivery == 2 and request.session['cart_sum'] == 0: return redirect('/', args)
    if request.POST:
        if delivery == 1: cart_form = MyCartForm1(request.POST, initial={'totalprice': float(request.session['cart_sum']), 'underwear':";".join(str(k[3])+str(k[2])+' '+str(k[7].encode('utf-8'))+" "+str(k[4])+"шт"  for k in request.session['cart']), 'purchase_number':str(new_purchase_number)+"/"+str(now.month), 'first_name': first_name, 'last_name': last_name})
        if delivery == 2: cart_form = MyCartForm2(request.POST, initial={'totalprice': float(request.session['cart_sum']), 'underwear':";".join(str(k[3])+str(k[2])+' '+str(k[7].encode('utf-8'))+" "+str(k[4])+"шт"  for k in request.session['cart']), 'purchase_number':str(new_purchase_number)+"/"+str(now.month), 'first_name': first_name, 'last_name': last_name})
        if cart_form.is_valid():
            cart_form.save()
            args['purchase_number']=request.POST.get('purchase_number','-')
            args['first_name']=request.POST.get('first_name','-')
            args['last_name']=request.POST.get('last_name','-')
            args['phone_number']=request.POST.get('phone_number','-')
            args['city']=request.POST.get('city','-')
            args['totalprice']=request.POST.get('totalprice','-')
            args['underwear']=request.POST.get('underwear','-')
            args['post_office']=request.POST.get('post_office','-')
            args['divisions']=request.POST.get('divisions','-')
            if args['divisions']=='a': args['divisions']="Доставка наложенным платежом"
            if args['divisions']=='b': args['divisions']="100% предоплата на карту Приват Банка*"
            args['comment']=request.POST.get('comment','-')


            """plaintext = get_template('email_purchase.txt')
            htmly = get_template('email_purchase.html')
            d = Context(args)
            subject, from_email, to = 'Новый заказ!', 'xxxxxxx@gmail.com', 'xxxxxx@gmail.com'
            text_content = plaintext.render(d)
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()"""



            return redirect('/thanks/')
        else:
            args['form'] = cart_form
    return render_to_response('cart.html', args)

def clean(request):
    request.session['cart'] = ""
    request.session['cart_pieces'] = 0
    request.session['cart_sum'] = 0
    args = {}
    args['pieces'] = request.session['cart_pieces']
    args['summ'] = request.session['cart_sum']
    args['username'] = auth.get_user(request).username
    try:
        current_series = request.session['current_series']
    except:
        current_series = 'ALL'
        request.session['current_series'] = 'ALL'
    return redirect('/'+current_series+'/page/1/')

def universal(request, htmlfile):
    args = {}
    try:
        args['pieces'] = request.session['cart_pieces']
        args['summ'] = request.session['cart_sum']
    except:
        args['pieces'] = 0
        args['summ'] = 0
    try:
        args['cart'] = request.session['cart']
    except:
        args['cart'] = ""
    args['username'] = auth.get_user(request).username
    return render_to_response(htmlfile, args)

def del_item(request):
    if 'item_id' in request.GET:
        item_id = int(request.GET['item_id'])
        cart_new = request.session['cart']
        request.session['cart_sum'] = request.session['cart_sum']-cart_new[item_id-1][6]
        request.session['cart_pieces'] = request.session['cart_pieces']-cart_new[item_id-1][4]
        cart_new.pop(item_id-1)
        request.session['cart_id']=request.session['cart_id']-1
        for i in range(item_id-1, len(cart_new)):
            cart_new[i][0]=cart_new[i][0]-1
        request.session['cart'] = cart_new
    args = {}
    args['cart'] = request.session['cart']
    args['pieces'] = request.session['cart_pieces']
    args['summ'] = request.session['cart_sum']
    args['username'] = auth.get_user(request).username
    return redirect('/cart/', args)


def contacts(request):
    args = {}
    args.update(csrf(request))
    try:
        args['pieces'] = request.session['cart_pieces']
        args['summ'] = request.session['cart_sum']
    except:
        args['pieces'] = 0
        args['summ'] = 0
    try:
        args['cart'] = request.session['cart']
    except:
        args['cart'] = ""
    args['username'] = auth.get_user(request).username
    if request.POST:
        args['first_name']=request.POST.get('first_name','-')
        args['email']=request.POST.get('email','-')
        args['comment']=request.POST.get('comment','-')
        args['login_error'] = []
        if args['first_name'] == "":
            args['login_error'] = args['login_error']+['Введите имя']
        else:
            args['login_error'] = args['login_error']+[False]
        if args['comment'] == "":
            args['login_error'] = args['login_error']+['Введите сообщение']
        else:
            args['login_error'] = args['login_error']+[False]
        try:
            validate_email(args['email'])
            """plaintext = get_template('email_feedback.txt')
            htmly = get_template('email_feedback.html')
            d = Context(args)
            subject, from_email, to = 'Новый отзыв!!!', 'xxxxxx@gmail.com', 'xxxxxx@gmail.com'
            text_content = plaintext.render(d)
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()"""
            if args['comment'] != "" and args['first_name'] != "" and args['email']!= "":
                return redirect('/thanks_feedback/')
        except:
            args['login_error'] = args['login_error']+['Введите верный e-mail']
    return render_to_response('contacts.html', args)


def thanks(request):
    args = {}
    args['pieces'] = request.session['cart_pieces']
    args['summ'] = request.session['cart_sum']
    args['username'] = auth.get_user(request).username
    args['cart'] = request.session['cart']
    request.session['cart'] = ""
    request.session['cart_pieces'] = 0
    request.session['cart_sum'] = 0
    return render_to_response('thanks.html', args)