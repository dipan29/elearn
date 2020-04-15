from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


from elearn import settings

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('cart/', include('cart.urls')),
    path('', include('accounts.urls')),
    path('', include('root.urls')),
    path('', include('courses.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('pinterest.html', TemplateView.as_view(template_name="pinterest-dd9f1.html"), name='pinterest'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
