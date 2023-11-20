from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from . import views

# urls
urlpatterns = [
    path('', views.index, name='index'),
    path('api/v1/hojas/', include('hojas.urls')),
    path('api/v1/auth/', include('authentication.urls')),
    path('admin/', admin.site.urls),
] + static( settings.STATIC_URL, document_root=settings.STATIC_ROOT, show_indexes=True )