from django.urls import path
from . import views  # ← This makes sure it's using blogapp.views

urlpatterns = [
    path('', views.index, name='index'),
    path('secondURL', views.secondURL, name='secondURL'),
    path('device/<int:device_id>', views.device, name='device'),
]


