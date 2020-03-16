from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, redirect, get_object_or_404
# Verification imports
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import send_mail
# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, FormView, RedirectView, ListView, DetailView, UpdateView, View

from courses.models import Category, Lesson, Course
from root.models import Enroll
from .models import User
from .forms import UserRegistrationForm, UserLoginForm, ProfileUpdateForm

from .tokens import account_activation_token
from validate_email import validate_email



def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(email=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('root:home')
    else:
        print('failed')
        return redirect('root:home')

class RegisterView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'accounts/form.html'
    success_url = '/login'

    extra_context = {
        'title': 'Register'
    }

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        return super().dispatch(self.request, *args, **kwargs)

    def get_success_url(self):
        return self.success_url

    def post(self, request, *args, **kwargs):

        user_form = self.form_class(data=request.POST)

        if user_form.is_valid():
            user = user_form.save(commit=False)
            email_valid = validate_email(user.email, verify=True)
            if(email_valid == None or email_valid!=True):
                invalid_email = True
                print("Invalid Email Address")
                return render(request, 'accounts/form.html', {'form': user_form, 'invalid_email': invalid_email})
            else:
                user.is_active = False
                password = user_form.cleaned_data.get("password1")
                current_site = get_current_site(request)
                mail_subject = 'Activate your Insta Worthy Academy account. Visit the link to activate'
                message = render_to_string('accounts/account_active_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.email)),
                    'token': account_activation_token.make_token(user),
                })
                email = send_mail(mail_subject, message, from_email='support@instaworthyacademy.com', recipient_list=[user.email])
                if email > 0:
                    user.set_password(password)
                    user.save()
                    return redirect('accounts:login')
                else:
                    return render(request, 'accounts/form.html', {'form': user_form})
        else:
            return render(request, 'accounts/form.html', {'form': user_form})


class LoginView(FormView):
    """
        Provides the ability to login as a user with an email and password
    """
    success_url = '/'
    form_class = UserLoginForm
    template_name = 'accounts/form.html'

    extra_context = {
        'title': 'Login'
    }

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        return super().dispatch(self.request, *args, **kwargs)

    def get_form_class(self):
        return self.form_class

    def form_valid(self, form):
        auth.login(self.request, form.get_user())

        return HttpResponseRedirect(self.get_success_url())
        # return super(Login, self).form_valid(form)

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        return self.render_to_response(self.get_context_data(form=form))


class LogoutView(RedirectView):
    """
    Provides users the ability to logout
    """
    url = '/login'

    def get(self, request, *args, **kwargs):
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return super(LogoutView, self).get(request, *args, **kwargs)


class EnrolledCoursesListView(ListView):
    model = Enroll
    template_name = 'courses/enrolled_courses.html'
    context_object_name = 'enrolls'

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.select_related('course').filter(user_id=self.request.user.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class StartLessonView(DetailView):
    model = Lesson
    template_name = 'lessons/lessons_by_course.html'
    context_object_name = 'lesson'

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = get_object_or_404(Course, slug=self.kwargs["slug"])
        context["lessons"] = self.model.objects.filter(course=course)
        context["course"] = course
        return context


class LessonView(DetailView):
    model = Lesson
    template_name = 'lessons/lessons_by_course.html'
    context_object_name = 'lesson'

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = get_object_or_404(Course, slug=self.kwargs["slug"])
        context["lessons"] = self.model.objects.filter(course=course)
        context["course"] = course
        return context


class ProfileUpdateView(UpdateView):
    model = User
    template_name = "accounts/profile.html"
    context_object_name = "user"
    form_class = ProfileUpdateForm
    success_url = reverse_lazy("accounts:my-profile")

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get_initial(self):
        return {"first_name": self.request.user.first_name, "last_name": self.request.user.last_name}

    def get_object(self, queryset=None):
        return get_object_or_404(self.model, email=self.request.user.email)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            obj = self.get_object()
            obj.first_name = self.get_initial()['first_name']
            obj.last_name = self.get_initial()['last_name']
            obj.save()
        return super().post(request, *args, **kwargs)
