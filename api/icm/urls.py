from django.urls import path
from . import views

urlpatterns = [
    path('', views.ICMView.as_view(), name='icm-get'),
]