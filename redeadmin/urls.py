from django.urls import path
from .views import cadastrar_servicos, editar_servicos, listar_servicos  


urlpatterns = [
    path('servicos/cadastrar', cadastrar_servicos, name='cadastrar_servicos'), 
    path('servicos/listar', listar_servicos, name='listar_servicos'),
    path('servicos/editar/<int:id>', editar_servicos, name='editar_servicos'),
]