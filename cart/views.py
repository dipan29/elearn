from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail


from courses.models import Course, Category
from root.models import Enroll, PageInfo, Discount
from .cart import Cart
from elearn.settings import COMPANY_NAME, COMPANY_EMAIL

@require_POST
@login_required(login_url=reverse_lazy('accounts:login'))
def cart_add_bundle(request, slug):
    cart = Cart(request)  # create a new cart object passing it the request object
    category = get_object_or_404(Category, slug=slug)
    discounted_value = 0
    courses = Course.objects.filter(category=category)
    try:
        discount = Discount.objects.get(category=category, code=request.POST.get('discount')).value
    except:
        discount = 0
    courses_added = 0
    for course in courses:
        if not Enroll.objects.filter(course=course, user_id=request.user.id).exists():
            courses_added += 1
            discounted_value += cart.add(course=course, quantity=1, update_quantity=False, discount=discount)
    return redirect('cart:cart_detail', last_discount=discounted_value , courses_added = courses_added)

@require_POST
@login_required(login_url=reverse_lazy('accounts:login'))
def cart_add(request, slug):
    cart = Cart(request)
    course = get_object_or_404(Course, slug=slug)
    discount_value = cart.add(course=course, quantity=1, update_quantity=False, discount=request.POST.get('discount'))
    return redirect('cart:cart_detail', last_discount=discount_value, courses_added = 1)

def cart_remove(request, slug):
    cart = Cart(request)
    course = get_object_or_404(Course, slug=slug)
    cart.remove(course)
    return redirect('cart:cart_detail')


def cart_detail(request, last_discount=0, courses_added=0):
    cart = Cart(request)
    context = {}
    context['cart'] = cart
    if(last_discount<0 or courses_added>0):
        ''' Print the link of paypal/payment to pay, amount to be paid is -1*last_discount'''
        info = PageInfo.objects.all()
        if(len(info)>0):
            info = info[0]
            context['pay_to'] = info.payment_id
            context['amount'] = -1*last_discount
            # message = "Please pay $ "+str(context['amount'])+" to the account "+str(context['pay_to'])+" in order to access your course right away, for queries please contact "+str(info.contact_number)
            message = """Hello,\nThank you for deciding to purchase our course. \nTo get full access to the course and it's benefits, please make the payment of {} {} shown during check out to {} through PayPal, Goods&Services. \nIn the note, please include the following details in this format :
                \nYour Name - Name of the Course.\n\nFailure to do so, please reply to this mail immediately with the mail id you paid through. \nYou will receive an Invoice of the payment and complete access to our courses once we have confirmed your payment.
                \nNote : It may take a bit of time to confirm the payment and give you access, but it will be done before 24 hours.\n\nMeanwhile, you can check out our Facebook Group - https://www.facebook.com/groups/2580480742199538/ and engage with the other group members!
                \n\nFor any further queries please mail to {} """.format(str(info.currency), str(context['amount']), str(context['pay_to']), COMPANY_EMAIL)
                
            send_mail(COMPANY_NAME+" | Payment of "+str(context['amount'])+" is Due", message , from_email=COMPANY_EMAIL, recipient_list=[request.user.email])
        else:
            context['pay_to'] = "Payment Id Uninitialized"
            context['amount'] = -1*last_discount
    else:
        context['discount'] = last_discount

    return render(request, 'cart/detail.html', context)


def cart_checkout(request, amount):
    carts = Cart(request)
    courses_added = 0
    for cart in carts:
        course = cart['course']
        courses_added += 1
        # course = get_object_or_404(Course, slug=course.slug)
        Enroll.objects.create(course=course, user_id=request.user.id)
    messages.success(request, 'Successfully checked out!')
    carts.clear()
    return redirect('cart:cart_detail', last_discount=-1*amount, courses_added=courses_added)
