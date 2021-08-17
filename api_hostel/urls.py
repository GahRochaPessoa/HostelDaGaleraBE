from api_hostel.hospede.views import *
from api_hostel.funcionario.views import *
from api_hostel.quarto_cama.views import *
from api_hostel.reserva.views import *
from api_hostel.pagamento.views import *
from api_hostel.relatorio.views import relatorioOcupacao
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
router.register(r'reserva',reservaViewSet)
router.register(r'statusreserva',statusreservaViewSet)
router.register(r'reservacama',reservacamaViewSet)
router.register(r'pagamento',pagamentoViewSet)
#router.register(r'relatorio',relatorioOcupacao)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('relatorio/',relatorioOcupacao),
]
