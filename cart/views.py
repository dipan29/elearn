from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail



from courses.models import Course
from root.models import Enroll, PageInfo
from .cart import Cart

@require_POST
@login_required(login_url=reverse_lazy('accounts:login'))
def cart_add(request, slug):
    cart = Cart(request)  # create a new cart object passing it the request object
    course = get_object_or_404(Course, slug=slug)
    discount_value = cart.add(course=course, quantity=1, update_quantity=False, discount=request.POST.get('discount'))
    return redirect('cart:cart_detail', last_discount=discount_value)


def cart_remove(request, slug):
    cart = Cart(request)
    course = get_object_or_404(Course, slug=slug)
    cart.remove(course)
    return redirect('cart:cart_detail')


def cart_detail(request, last_discount=0):
    cart = Cart(request)
    context = {}
    context['cart'] = cart
    if(last_discount<0):
        ''' Print the link of paypal/payment to pay, amount to be paid is -1*last_discount'''
        info = PageInfo.objects.all()
        if(len(info)>0):
            info = info[0]
            context['pay_to'] = info.payment_id
            context['amount'] = -1*last_discount
            # message = "Please pay $ "+str(context['amount'])+" to the account "+str(context['pay_to'])+" in order to access your course right away, for queries please contact "+str(info.contact_number)
            message = "Hello,<br />Thank you for deciding to purchase our course. <br/>To get full access to the course and it's benefits, please make the payment of $" + str(context['amount']) + " shown during check out to "+ str(context['pay_to']) + " through PayPal, Goods&Services. <br />In the note, please include the following details in this format :"
            message += "<br />Your Name - Name of the Course.<br /><br />Failure to do so, please reply to this mail immediately with the mail id you paid through. <br />You will receive an Invoice of the payment and complete access to our courses once we have confirmed your payment."
            message += "<br />Note : It may take a bit of time to confirm the payment and give you access, but it will be done before 24 hours.<br /><br />Meanwhile, you can check out our Facebook Group - https://www.facebook.com/groups/2580480742199538/ and engage with the other group members!";
            message += "<br />For any further queries please mail to support@instaworthyacademy.com"
            send_mail("IWA | Payment of $ "+str(context['amount'])+" is Due", message , from_email='support.iwa@mindwebs.org', recipient_list=[request.user.email])
        else:
            context['pay_to'] = "Payment Id Uninitialized"
            context['amount'] = -1*last_discount
    else:
        context['discount'] = last_discount

    return render(request, 'cart/detail.html', context)


def cart_checkout(request, amount):
    carts = Cart(request)
    for cart in carts:
        course = cart['course']
        # course = get_object_or_404(Course, slug=course.slug)
        Enroll.objects.create(course=course, user_id=request.user.id)
    messages.success(request, 'Successfully checked out!')
    carts.clear()
    return redirect('cart:cart_detail', last_discount=-1*amount)
