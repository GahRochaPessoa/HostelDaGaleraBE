from django.urls import path

from . import views

urlpatterns = [
    path('', views.hospede, name='hospede'),
]