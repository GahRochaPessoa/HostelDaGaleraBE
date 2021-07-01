"""api_hostel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from api_hostel.hospede.views import *
from api_hostel.funcionario.views import *
from api_hostel.quarto_cama.views import *
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'hospede',hospedesViewSet)
router.register(r'funcionario',funcionarioViewSet)
router.register(r'tipofuncionario',tipofuncionarioViewSet)
router.register(r'quarto',quartoViewSet)
router.register(r'tipoquarto',tipoquartoViewSet)
router.register(r'cama',camaViewSet)
router.register(r'tipocama',tipocamaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))
]
