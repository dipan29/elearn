from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from elearn import settings

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('cart/', include('cart.urls')),
    path('', include('accounts.urls')),
    path('', include('root.urls')),
    path('', include('courses.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
