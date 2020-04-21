from decimal import Decimal
from django.conf import settings

from courses.models import Course
from root.models import Discount, PageInfo


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_SLUG)
        if not cart:
            cart = self.session[settings.CART_SESSION_SLUG] = {}
        self.cart = cart

    def add(self, course, quantity=1, update_quantity=False, discount=0):
        course_slug = str(course.slug)
        discount_value = 0
        if course_slug not in self.cart:
            try:
                if(str(discount).isnumeric()):
                    value = (int(course.price)*discount)//100
                else:
                    discont = Discount.objects.get(course=course, code=discount)
                    value = (Discount.objects.get(code=discount).value*int(course.price))//100
                discount_value += value
            except:
                discount_value = 0
            self.cart[course_slug] = {'quantity': 0, 'price': str(int(course.price)-discount_value)}
        if update_quantity:
            self.cart[course_slug]['quantity'] = quantity
        else:
            self.cart[course_slug]['quantity'] += quantity
        self.save()
        return discount_value

    def save(self):
        self.session[settings.CART_SESSION_SLUG] = self.cart
        self.session.modified = True

    def remove(self, course):
        course_slug = str(course.slug)
        if course_slug in self.cart:
            del self.cart[course_slug]
            self.save()

    def __iter__(self):
        course_slugs = self.cart.keys()
        courses = Course.objects.filter(slug__in=course_slugs)
        for course in courses:
            self.cart[str(course.slug)]['course'] = course

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def has_course(self, course):
        course_slug = str(course.slug)
        return course_slug in self.cart

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_SLUG]
        self.session.modified = True
