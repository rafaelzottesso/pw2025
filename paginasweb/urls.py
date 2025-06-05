from django.urls import path
from .views import IndexView, SobreView
from .views import CampusCreate, CursoCreate, TipoSolicitacaoCreate, StatusCreate, AlunoCreate, ServidorCreate, SolicitacaoCreate, HistoricoCreate
from .views import CampusUpdate, CursoUpdate, TipoSolicitacaoUpdate, StatusUpdate, AlunoUpdate, ServidorUpdate, SolicitacaoUpdate, HistoricoUpdate
from .views import CampusDelete, CursoDelete, TipoSolicitacaoDelete, StatusDelete, AlunoDelete, ServidorDelete, SolicitacaoDelete, HistoricoDelete
from .views import CampusList, CursoList


urlpatterns = [
    
    path('', IndexView.as_view(), name='index'),  # URL para a página inicial
    path("sobre/", SobreView.as_view(), name="sobre"),

    path("cadastrar/campus/", CampusCreate.as_view(), name="cadastrar-campus"),  # URL para criar um novo campus
    path("cadastrar/curso/", CursoCreate.as_view(), name="cadastrar-curso"),  # URL para criar um novo curso
    path("cadastrar/tipo-solicitacao/", TipoSolicitacaoCreate.as_view(), name="cadastrar-tipo-solicitacao"),  # URL para criar um novo tipo de solicitação
    path("cadastrar/status/", StatusCreate.as_view(), name="cadastrar-status"),  # URL para criar um novo status
    path("cadastrar/aluno/", AlunoCreate.as_view(), name="cadastrar-aluno"),  # URL para criar um novo aluno
    path("cadastrar/servidor/", ServidorCreate.as_view(), name="cadastrar-servidor"),  # URL para criar um novo servidor
    path("cadastrar/solicitacao/", SolicitacaoCreate.as_view(), name="cadastrar-solicitacao"),  # URL para criar uma nova solicitação
    path("cadastrar/historico/", HistoricoCreate.as_view(), name="cadastrar-historico"),  # URL para criar um novo histórico

    # As URLs para editar precisam receber na URL o ID do objeto que deve ser excluído
    # Por isso, usamos <int:pk> para capturar o ID e passá-lo para a view correspondente
    # <int:pk> significa que estamos esperando um número inteiro (int) e o nome do parâmetro é pk (primary key)
    # <tipo_em_python:nome_do_parametro>
    path("editar/campus/<int:pk>/", CampusUpdate.as_view(), name="editar-campus"),
    path("editar/curso/<int:pk>/", CursoUpdate.as_view(), name="editar-curso"),
    path("editar/tipo-solicitacao/<int:pk>/", TipoSolicitacaoUpdate.as_view(), name="editar-tipo-solicitacao"),
    path("editar/status/<int:pk>/", StatusUpdate.as_view(), name="editar-status"),
    path("editar/aluno/<int:pk>/", AlunoUpdate.as_view(), name="editar-aluno"),
    path("editar/servidor/<int:pk>/", ServidorUpdate.as_view(), name="editar-servidor"),
    path("editar/solicitacao/<int:pk>/", SolicitacaoUpdate.as_view(), name="editar-solicitacao"),
    path("editar/historico/<int:pk>/", HistoricoUpdate.as_view(), name="editar-historico"),

    # O excluir também precisa receber o ID do objeto que deve ser excluído
    # e passá-lo para a view correspondente
    path("excluir/campus/<int:pk>/", CampusDelete.as_view(), name="excluir-campus"),
    path("excluir/curso/<int:pk>/", CursoDelete.as_view(), name="excluir-curso"),
    path("excluir/tipo-solicitacao/<int:pk>/", TipoSolicitacaoDelete.as_view(), name="excluir-tipo-solicitacao"),
    path("excluir/status/<int:pk>/", StatusDelete.as_view(), name="excluir-status"),
    path("excluir/aluno/<int:pk>/", AlunoDelete.as_view(), name="excluir-aluno"),
    path("excluir/servidor/<int:pk>/", ServidorDelete.as_view(), name="excluir-servidor"),
    path("excluir/solicitacao/<int:pk>/", SolicitacaoDelete.as_view(), name="excluir-solicitacao"),
    path("excluir/historico/<int:pk>/", HistoricoDelete.as_view(), name="excluir-historico"),  # URL para excluir um histórico

    path("listar/campi/", CampusList.as_view(), name="listar-campus"),
    path("listar/cursos/", CursoList.as_view(), name="listar-curso"),
]
