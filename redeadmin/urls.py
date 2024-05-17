from django.urls import path
from .views import servicos_views, usuario_views


urlpatterns = [
    path('servicos/cadastrar', servicos_views.cadastrar_servicos, name='cadastrar_servicos'), 
    path('servicos/listar', servicos_views.listar_servicos, name='listar_servicos'),
    path('servicos/editar/<int:id>', servicos_views.editar_servicos, name='editar_servicos'),
    path('usuarios/cadastrar', usuario_views.cadastrar_usuario, name='cadastrar_usuario'),
    path('usuarios/listar', usuario_views.listar_usuarios, name='cadastrar_usuarios'),
    path('usuarios/editar/<int:id>', usuario_views.editar_usuario, name='editar_usuario'),
]