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
            message = "Please pay $ "+str(context['amount'])+" to the account "+str(context['pay_to'])+" in order to access your course right away, for queries please contact "+str(info.contact_number)
            send_mail("Payment of $ "+str(context['amount'])+" is due", message , from_email='support@instaworthyacademy.com', recipient_list=[request.user.email])
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
