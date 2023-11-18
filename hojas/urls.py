from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListCreateHojaAPIView.as_view(), name='get_post_hojas'),
    path('<int:pk>/', views.RetrieveUpdateDestroyHojaAPIView.as_view(), name='get_delete_update_hoja'),
]