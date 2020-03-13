from django.http import Http404, HttpResponseForbidden
from django.shortcuts import render
from django.views.generic import DetailView, ListView, FormView
from django.views import View
from django.urls import reverse
from django.views.generic.detail import SingleObjectMixin

from cart.cart import Cart
from courses.models import Course, Category, Comment
from root.models import Enroll
from .forms import CommentForm


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/details.html'
    context_object_name = 'course'

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()

        slug = self.kwargs.get(self.slug_url_kwarg)
        slug_field = self.get_slug_field()
        queryset = queryset.filter(**{slug_field: slug})
        try:
            # Get the single item from the filtered queryset
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404("No %(verbose_name)s found matching the query" %
                          {'verbose_name': self.model._meta.verbose_name})
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()        
        course = self.get_object(self.get_queryset())
        context['comments'] = Comment.objects.filter(course=course).order_by("-created_date")
        if self.request.user.is_authenticated:
            enrollment = Enroll.objects.filter(course=course, user_id=self.request.user.id)
            if enrollment.exists():
                context['is_enrolled'] = True
                context['has_access'] = True if enrollment[0].enable_access == True else False
            else:
                cart = Cart(self.request)
                context['is_in_cart'] = cart.has_course(course)
        else:
            cart = Cart(self.request)
            context['is_in_cart'] = cart.has_course(course)
        return context

class CourseCommentForm(SingleObjectMixin, FormView):
    template_name = 'courses/details.html'
    form_class = CommentForm
    model = Course

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.course = Course.objects.get(slug=self.kwargs['slug'])
            obj.save()
            print("The form was valid")
        return super().post(request, *args, **kwargs)


    def get_success_url(self):
        return reverse('courses:course-details', kwargs={'slug': self.object.slug})

class CourseDetail(View):

    def get(self, request, *args, **kwargs):
        view = CourseDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CourseCommentForm.as_view()
        return view(request, *args, **kwargs)




class CoursesByCategoryListView(ListView):
    model = Course
    template_name = 'courses/courses_by_category.html'
    context_object_name = 'courses'

    def get_queryset(self):
        category = Category.objects.get(slug=self.kwargs['slug'])
        return self.model.objects.filter(category_id=category.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Category.objects.get(slug=self.kwargs['slug'])
        context['category'] = category
        context['categories'] = Category.objects.all()
        return context
