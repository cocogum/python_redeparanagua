from django.urls import path
from django.urls import reverse_lazy
from .views import servicos_views, usuario_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('servicos/cadastrar', servicos_views.cadastrar_servicos, name='cadastrar_servicos'), 
    path('servicos/listar', servicos_views.listar_servicos, name='listar_servicos'),
    path('servicos/editar/<int:id>', servicos_views.editar_servicos, name='editar_servicos'),
    path('usuarios/cadastrar', usuario_views.cadastrar_usuario, name='cadastrar_usuario'),
    path('usuarios/listar', usuario_views.listar_usuarios, name='cadastrar_usuarios'),
    path('usuarios/editar/<int:id>', usuario_views.editar_usuario, name='editar_usuario'),
    path('autenticacao/login', auth_views.LoginView.as_view(), name='logar_usuario'),
    path('autenticacao/logout', auth_views.LogoutView.as_view(), name='deslogar_usuario'),
    path('alterar_senha', auth_views.PasswordChangeView.as_view(
        success_url=reverse_lazy('listar_servicos')), name='alterar_senha'),
    path('resetar_senha', auth_views.PasswordResetView.as_view(), name='resetar_senha'),
    path('resetar_senha_sucesso', auth_views.PasswordResetView.as_view(),
         name='resetar_senha_sucesso'),
    path('resetar_senha/<str:uidb64>/<str:token>', auth_views.PasswordResetConfirmView.as_view(),
         name='resetar_senha-confirmar'),
    path('resetar_senha/feito', auth_views.PasswordChangeDoneView.as_view(),
         name='resetar_senha_feito'),
    
]