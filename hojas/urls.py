from django.urls import path
from .views import ImageView, MapView


urlpatterns = [
    path('upload/', ImageView.as_view(), name='image-upload'),
    path('upload/map/', MapView.as_view(), name='map-upload'),
]