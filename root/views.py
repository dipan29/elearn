from django.shortcuts import render
from django.views.generic import ListView

from courses.models import Course, Category, MasterCategory
from .models import Testimonial, PageInfo


def index(request):
    return render(request, 'index.html', {})


class HomeListView(ListView):
    model = Course
    template_name = 'index.html'
    context_object_name = 'courses'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            slug = self.kwargs['slug']
        except:
            slug = None
        if(slug):
            m_category = MasterCategory.objects.get(slug=slug)
            categories = Category.objects.filter(master_category=m_category)
            context['top_courses'] = self.model.objects.filter(category__in=categories).order_by('?')
            context['sub_categories'] = categories
        else:
            context['no_slug'] = True
            context['m_categories'] = MasterCategory.objects.all()
        context['testimonials'] = Testimonial.objects.all()
        return context


class SearchView(ListView):
    model = Course
    template_name = 'search.html'
    context_object_name = 'courses'
    paginate_by = 10

    def get_queryset(self):
        return self.model.objects.filter(title__icontains=self.request.GET['q'])

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['search_results'] = self.get_queryset()
            return context


def handler404(request, exception):
    return render(request, '404.html')